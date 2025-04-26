scores = [85, 92, 88, 76, 95, 89, 100, 67, 93, 81]

# Find top 3 highest scores
top_scores = sorted(scores, reverse=True)[:3]

average_score = sum(scores) / len(scores)

print("Top 3 Scores:", top_scores)
print("Average Score:", average_score)
