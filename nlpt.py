import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.metrics import jaccard_distance
from nltk import FreqDist
import json

# Load the JSON data
with open('legal functionalities and services.json', 'r', encoding='utf-8') as json_file:
    legal_functionalities = json.load(json_file)["functionalities"]

# Tokenize and preprocess user query
def preprocess_query(query):
    # Tokenize the query
    tokens = word_tokenize(query.lower())

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    return filtered_tokens

# Calculate Jaccard Similarity
def jaccard_similarity(query, keywords):
    query_set = set(query)
    keywords_set = set(keywords)
    return 1 - jaccard_distance(query_set, keywords_set)

# Find the most relevant case based on user query
def find_relevant_case(user_query):
    user_tokens = preprocess_query(user_query)
    case_scores = []

    for case in legal_functionalities:
        keywords = case["keywords"]
        description = case["description"]
        similarity = jaccard_similarity(user_tokens, keywords)
        case_scores.append((case, similarity))

    # Sort cases by similarity score
    sorted_cases = sorted(case_scores, key=lambda x: x[1], reverse=True)

    return sorted_cases[0][0] if sorted_cases else None

# Main function to provide information about citizens' rights
def get_citizens_rights(user_query):
    relevant_case = find_relevant_case(user_query)

    if relevant_case:
        category = relevant_case["name"]
        description = relevant_case["description"]
        return f"Category: {category}\nDescription: {description}"
    else:
        return "Sorry, I couldn't find relevant information for your query."

# Example usage:
user_query = "What are my rights as an employee under Indian labor laws?"
rights_info = get_citizens_rights(user_query)
print(rights_info)
