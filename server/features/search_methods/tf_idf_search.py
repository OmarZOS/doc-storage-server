import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize the TfidfVectorizer
vectorizer = TfidfVectorizer()

# File path to store the backup
backup_file = "tfidf_matrices_backup.pkl"

# Function to load the backup from file
def load_backup():
    try:
        return joblib.load(backup_file)
    except FileNotFoundError:
        return {}

# Function to save the backup to file
def save_backup(matrices):
    joblib.dump(matrices, backup_file)

# Dictionary to store the matrices with search_keys
tfidf_matrices = load_backup()


def add_many_tokens(search_key, new_tokens:list):
    global tfidf_matrices

    # Check if the search_key already exists in the matrices dictionary
    if search_key not in tfidf_matrices:
        # Create a new matrix for the search_key
        tfidf_matrices[search_key] = {
            "tokens_set": [],
            "matrix": None
        }

    # Get the tokens_set and matrix for the search_key
    tokens_set = tfidf_matrices[search_key]["tokens_set"]
    tfidf_matrix = tfidf_matrices[search_key]["matrix"]

    # Add the new tokens to the tokens_set
    tokens_set.extend(new_tokens)

    # Update the TF-IDF matrix incrementally
    new_tokens_vector = vectorizer.transform(new_tokens)
    if tfidf_matrix is None:
        tfidf_matrix = new_tokens_vector
    else:
        tfidf_matrix = cosine_similarity(new_tokens_vector, tfidf_matrix)

    # Update the matrix in the dictionary
    tfidf_matrices[search_key]["matrix"] = tfidf_matrix

    # Save the updated matrices to the backup file
    save_backup(tfidf_matrices)


def add_token(search_key, new_token):
    global tfidf_matrices

    # Check if the search_key already exists in the matrices dictionary
    if search_key not in tfidf_matrices:
        # Create a new matrix for the search_key
        tfidf_matrices[search_key] = {
            "tokens_set": [],
            "matrix": None
        }

    # Get the tokens_set and matrix for the search_key
    tokens_set = tfidf_matrices[search_key]["tokens_set"]
    tfidf_matrix = tfidf_matrices[search_key]["matrix"]

    # Add the new tokens to the tokens_set
    tokens_set.append(new_token)

    # Update the TF-IDF matrix incrementally
    new_tokens_vector = vectorizer.transform(new_tokens)
    if tfidf_matrix is None:
        tfidf_matrix = new_tokens_vector
    else:
        tfidf_matrix = cosine_similarity(new_tokens_vector, tfidf_matrix)

    # Update the matrix in the dictionary
    tfidf_matrices[search_key]["matrix"] = tfidf_matrix

    # Save the updated matrices to the backup file
    save_backup(tfidf_matrices)




def get_most_similar_tokens(search_key, new_token, K):
    # Get the tokens_set and matrix for the search_key
    tokens_set = tfidf_matrices[search_key]["tokens_set"]
    tfidf_matrix = tfidf_matrices[search_key]["matrix"]

    # Transform the new token using the TF-IDF vectorizer
    new_token_vector = vectorizer.transform([new_token])

    # Compute similarity scores between the new token and all existing tokens
    similarity_scores = cosine_similarity(new_token_vector, tfidf_matrix)

    # Get the indices of the top K most similar tokens
    top_k_indices = similarity_scores.argsort()[0][::-1][:K]

    # Get the corresponding tokens
    top_k_tokens = [tokens_set[i] for i in top_k_indices]

    return top_k_tokens

# # Add some initial tokens for the "fruits" search_key
# add_tokens("fruits", ["apple", "banana", "orange"])

# # Get the most similar tokens for a new token in the "fruits" search_key
# similar_tokens = get_most_similar_tokens("fruits", "fruit", 2)
# print(similar_tokens)

# # Add some initial tokens for the "animals" search_key
# add_tokens("animals", ["dog", "cat", "bird"])

# # Get the most similar tokens for a new token in the "animals" search_key
# similar_tokens = get_most_similar_tokens("animals", "pet", 2)
# print(similar_tokens)
