import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV file
data = pd.read_csv('student_data.csv')  # Replace with your data source

# Calculate correlation between study time and exam scores
correlation = data['StudyTime'].corr(data['ExamScore'])

# Create a scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(data['StudyTime'], data['ExamScore'])
plt.title(f"Study Time vs. Exam Scores (Correlation: {correlation:.2f})")
plt.xlabel('Study Time (hours)')
plt.ylabel('Exam Score')
plt.grid(True)
plt.show()

# Additional visualization using seaborn (optional)
sns.jointplot(x='StudyTime', y='ExamScore', data=data, kind='reg')
plt.show()
