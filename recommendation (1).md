# Product Recommendation

## Introduction

This document describes the product recommendation feature of the system. The system will recommend products to users based on their past purchases  history. The recommendation system will use collaborative filtering to recommend products to users.

## Recommendation Algorithm 1

The recommendation algorithm is based on collaborative filtering. Collaborative filtering is a technique used by recommendation systems to make predictions about the interests of a user by collecting preferences from many users. The recommendation algorithm uses the following steps:

1. Calculate the similarity between users based on their past purchases history.
2. For each user, find the most similar users.
3. Recommend products to the user based on the products purchased by the most similar users.

The recommendation algorithm uses the following formula to calculate the similarity between users:

```
similarity(u, v) = sum((r_ui - r_u)(r_vi - r_v)) / sqrt(sum((r_ui - r_u)^2) * sum((r_vi - r_v)^2))
```

where:
- `similarity(u, v)` is the similarity between users `u` and `v`.
- `r_ui` is the rating of user `u` for item `i`.
- `r_u` is the average rating of user `u`.
- `r_vi` is the rating of user `v` for item `i`.
- `r_v` is the average rating of user `v`.

The recommendation algorithm uses the following formula to calculate the most similar users

```
most_similar_users(u) = argmax(similarity(u, v))
```

where:
- `most_similar_users(u)` is the list of most similar users to user `u`.
- `argmax` is the function that returns the index of the maximum value in the list.

The recommendation algorithm recommends products to the user based on the products purchased by the most similar users.

The recommendation algorithm uses the following formula to calculate the Recommended products

```
recommended_products(u) = argmax(sum(similarity(u, v) * r_vi))
```

where:
- `recommended_products(u)` is the list of recommended products to user `u`.
- `argmax` is the function that returns the index of the maximum value in the list.

The recommendation algorithm uses the following formula to calculate rating of user

```
rating(u, i) = sum(similarity(u, v) * r_vi) / sum(similarity(u, v))
```

where:
- `rating(u, i)` is the rating of user `u` for item `i`.


## Recommendation Algorithm 2

### APACHE SPARK ALS

The recommendation algorithm is based on collaborative filtering. Collaborative filtering is a technique used by recommendation systems to make predictions about the interests of a user by collecting preferences from many users. The recommendation algorithm uses the following steps:

1. Load the user-product interactions data.
2. Train the ALS model using the user-product interactions data.
3. Make predictions for the user-product interactions data.
4. Recommend products to users based on the predictions.

The recommendation algorithm uses the Apache Spark ALS (Alternating Least Squares) algorithm to train the model. The ALS algorithm is a matrix factorization algorithm that factorizes the user-product interactions matrix into two lower-dimensional matrices: the user matrix and the product matrix. The ALS algorithm minimizes the squared error between the predicted ratings and the actual ratings.

The recommendation algorithm uses the following formula to calculate the predicted rating of user `u` for product `i`:

```
rating(u, i) = user_matrix(u) * product_matrix(i)
```

where:
- `rating(u, i)` is the predicted rating of user `u` for product `i`.
- `user_matrix(u)` is the user matrix for user `u`.
- `product_matrix(i)` is the product matrix for product `i`.

The recommendation algorithm uses the following formula to recommend products to user `u`:

```
recommended_products(u) = argmax(rating(u, i))
```

where:
- `recommended_products(u)` is the list of recommended products to user `u`.
- `argmax` is the function that returns the index of the maximum value in the list.



## Project Structure

The project structure for the recommendation API is as follows:

```

recommendation_api/
    ├── app.py
    ├── recommendation.py
    ├── requirements.txt
    └── README.md
```

1. `app.py`: This is the main file that contains the Flask application and the API endpoints.
2. `recommendation.py`: This file contains the implementation of the recommendation algorithm.
3. `requirements.txt`: This file contains the list of Python packages required for the project.
4. `README.md`: This file contains the documentation for the project.

## Recommendation API Endpoints

1. POST /api/recommendation/recommend : This endpoint accepts a list of user-product interactions and returns a list of recommended products for each user.

### Product Recommendation

#### Expected Input

The input to the recommendation API is a list of user-product interactions. Each interaction is represented as a dictionary with key-value pairs. The keys represent the user ID and the product ID, and the values represent the interaction strength. For example:

```json
{
    "data": [
        {"user_id":101, "product_id": 1, "product_id": 3, "product_id": 4},
        {"user_id":102, "product_id": 2, "product_id": 1},
        {"user_id":103, "product_id": 3, "product_id": 2, "product_id": 4},
        ...
    ]
}
```

#### Response

The response from the recommendation API is a list of recommended products for each user. Each user is represented as a dictionary with key-value pairs. The keys represent the user ID, and the values represent the recommended products. For example:

```json
{
    "status": "success",
    "data": [
        {
            "user_id": 101,
            "recommended_products": [1, 2, 4]
        },
        {
            "user_id": 102,
            "recommended_products": [3, 4]
        },
        {
            "user_id": 103,
            "recommended_products": [1, 2]
        },
        ...
    ]
}
```
