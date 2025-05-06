# Multiple Return Values for Grades

def analyze_scores(name, score1, score2, score3):
    average = (score1 + score2 + score3) / 3
    return (name, average)

result = analyze_scores(name="Akash", score1=85, score2=90, score3=80)
print(result)
