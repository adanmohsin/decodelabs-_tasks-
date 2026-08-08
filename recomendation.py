# AI Recommendation Logic
# Project 3 - Artificial Intelligence

print("===================================")
print("     AI Recommendation System")
print("===================================")

# Available items with their genres
movies = {
    "Inception": ["sci-fi", "action", "thriller"],
    "Interstellar": ["sci-fi", "drama"],
    "The Dark Knight": ["action", "crime", "thriller"],
    "Toy Story": ["animation", "comedy"],
    "The Notebook": ["romance", "drama"],
    "Avengers": ["action", "sci-fi"],
}

# Take user preferences
user_input = input(
    "\nEnter your favorite genres (e.g. action, sci-fi): "
)

# Convert input into a list
preferences = [
    genre.strip().lower()
    for genre in user_input.split(",")
]

# Find matching movies
recommendations = []

for movie, genres in movies.items():

    score = 0

    for preference in preferences:
        if preference in genres:
            score += 1

    if score > 0:
        recommendations.append((movie, score))

# Sort recommendations by matching score
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display recommendations
print("\nRecommended Movies:")

if recommendations:
    for movie, score in recommendations:
        print(f"- {movie} (Match Score: {score})")
else:
    print("Sorry, no matching movies found.")

print("\nThank you for using the AI Recommendation System!")