import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix
import numpy as np

def load_wine_dataframes():
    try:
        wine_data_2019_df = pd.read_csv('data_files/2019 KDI.csv')
        wine_data_2020_df = pd.read_csv('data_files/2020 KDI.csv')
        return wine_data_2019_df, wine_data_2020_df
    except Exception as e:
        print(f"Error loading wine data: {e}")
        return None, None

def preprocess_wine_data(wine_data_df):
    filtered_data = wine_data_df[wine_data_df['ItemQuantity'] > 0].dropna(subset=['ItemName'])
    return filtered_data

def generate_wine_customer_item_matrix_sparse(wine_data_df):
    customer_item_matrix = wine_data_df.pivot_table(index='LoyaltyNumber', columns='ItemName', values='ItemQuantity', aggfunc='sum', fill_value=0)
    customer_item_matrix_sparse = csr_matrix(customer_item_matrix.values)
    return customer_item_matrix_sparse, customer_item_matrix.index, customer_item_matrix.columns

def find_similar_customers(customer_index, customer_item_matrix_sparse, n_similar=5):
    target_customer_vector = customer_item_matrix_sparse[customer_index].reshape(1, -1)
    similarities = cosine_similarity(customer_item_matrix_sparse, target_customer_vector, dense_output=False)
    similar_indices = np.argsort(-similarities.toarray().ravel())[1:n_similar+1]  # Exclude self, hence [1:n+1]
    return similar_indices

def recommend_items_for_customer(customer_item_matrix_sparse, similar_customer_indices, item_columns):
    item_columns_list = item_columns.tolist()  # Convert Pandas Index to a list for safe indexing
    
    # Ensure item_scores is in a dense format before summing
    item_scores_dense = customer_item_matrix_sparse[similar_customer_indices].toarray()
    item_scores_summed = np.sum(item_scores_dense, axis=0)
    
    # Get indices of top 3 items
    top_item_indices = np.argsort(-item_scores_summed)[:3]
    recommended_items = [item_columns_list[i] for i in top_item_indices]
    return recommended_items

def recommend_for_customer(loyalty_number):
    # Main execution flow
    wine_data_2019_df, wine_data_2020_df = load_wine_dataframes()
    if wine_data_2019_df is not None and wine_data_2020_df is not None:
        wine_data_df = pd.concat([wine_data_2019_df, wine_data_2020_df], ignore_index=True)
        processed_wine_data = preprocess_wine_data(wine_data_df)
        customer_item_matrix_sparse, customer_indices, item_columns = generate_wine_customer_item_matrix_sparse(processed_wine_data)
        
        try:
            customer_number = loyalty_number
            if customer_number in customer_indices.to_numpy():
                customer_index = np.where(customer_indices == customer_number)[0][0]
                similar_customer_indices = find_similar_customers(customer_index, customer_item_matrix_sparse)
                recommended_items = recommend_items_for_customer(customer_item_matrix_sparse, similar_customer_indices, item_columns)
                print(f"Top 3 recommended items for Customer {customer_number}: {recommended_items}")
                return recommended_items
            else:
                print("LoyaltyNumber not found in the dataset.")
                return 'Not Found'
        except ValueError:
            print("Invalid LoyaltyNumber. Please enter a numeric value.")
    else:
        print("Failed to load wine data.")