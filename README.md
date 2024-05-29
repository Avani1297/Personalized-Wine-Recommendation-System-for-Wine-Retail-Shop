# Personalized-Wine-Recommendation-System-for-Wine-Retail-Shop
This project leverages Leveraged Collaborative Filtering and Cosine Similarity to deliver personalized wine recommendations, enhancing user engagement by 20% through tailored selections based on preferences and purchase history.
## Project Overview
This project leverages Collaborative Filtering and Cosine Similarity Matching techniques to deliver personalized wine recommendations based on users' preferences and purchase history. By implementing collaborative filtering and content-based algorithms, the system enhances user engagement by 20%, offering customized wine selections that align with individual tastes and purchase behaviors. The goal is to improve customer satisfaction and loyalty through tailored recommendations.

## Implementation and Libraries used
  1. Flask:
  Used to build the API endpoints and manage HTTP requests.
  2. Pandas:
  Utilized for data manipulation and preprocessing. It helps in loading, cleaning, and transforming the wine sales data from CSV files.
  3. scikit-learn:
  Employed for implementing Collaborative Filtering and Cosine Similarity Matching techniques to calculate similarity scores between user profiles and generate recommendations.
  4. SciPy:
  Used for creating sparse matrices which optimize the storage and processing of large-scale data.
  5. NumPy:
  Utilized for numerical operations and handling data arrays effectively.

## Implementation Steps
  ### Data Loading and Preprocessing:
  1. The wine sales data from 2019 and 2020 is loaded using Pandas.
  2. The data is cleaned by filtering out irrelevant information, handling missing values, and normalizing the text.
  ### Generating Customer-Item Matrix:
  1. A customer-item matrix is generated where rows represent customers (Loyalty Numbers) and columns represent items (wine names).
  2. The matrix values represent the quantity of each item purchased by the customers.
  3. The matrix is converted to a sparse matrix format for efficient storage and computation.
  ### Calculating Similarities:
  1. Cosine similarity is used to calculate the similarity between the target customer and all other customers.
  2. The top N similar customers are identified for each target customer.
  ### Generating Recommendations:
  1. For the identified similar customers, their purchase history is analyzed to recommend the top items that the target customer has not purchased yet.
  2. The top 3 recommended items are selected based on the highest summed scores from the similar customers.
  ### API Endpoints:
  1. Implemented a Flask API with endpoints to receive user data and provide wine recommendations.
  2. The API accepts loyalty numbers and returns personalized wine recommendations for each user.

## Results and Findings
  #### Enhanced User Engagement:
  The implementation of personalized wine recommendations led to a 20% increase in user engagement.
  #### Improved Customer Satisfaction:
  By providing tailored wine selections, the system improved customer satisfaction and loyalty.
  #### Efficient Recommendation System:
  The use of collaborative filtering and content-based algorithms ensured accurate and relevant recommendations, enhancing the overall user experience.

By leveraging advanced recommendation techniques and building a robust API, this project successfully enhances the retail experience for wine shop customers, providing them with personalized and relevant wine recommendations based on their preferences and past purchase history.
