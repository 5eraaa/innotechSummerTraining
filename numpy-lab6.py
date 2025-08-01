import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# 1. Student Exam Scores Analysis
np.random.seed(42)
scores = np.random.normal(70, 10, 100)
plt.figure(figsize=(10, 4))
plt.scatter(scores, np.zeros(100) + np.random.normal(0, 0.05, 100), alpha=0.6)
plt.title('Dot Plot of Exam Scores')
plt.xlabel('Scores')
plt.yticks([])
plt.show()
plt.figure(figsize=(10, 4))
plt.hist(scores, bins=15, edgecolor='black')
plt.title('Histogram of Exam Scores')
plt.xlabel('Scores')
plt.ylabel('Frequency')
plt.show()
z_scores = (scores - np.mean(scores)) / np.std(scores)
outliers = scores[(z_scores > 2) | (z_scores < -2)]
print(f"Outliers: {outliers}")

# 2. Fruit Sales Distribution
fruits = ['Apples', 'Bananas', 'Oranges', 'Grapes', 'Strawberries']
sales = np.random.randint(50, 200, size=5)
explode = [0.1 if s == max(sales) else 0 for s in sales]
plt.figure(figsize=(8, 8))
plt.pie(sales, labels=fruits, explode=explode, autopct='%1.1f%%', shadow=True)
plt.title('Fruit Sales Distribution')
plt.show()

# 3. Temperature vs. Ice Cream Sales
np.random.seed(42)
temp = np.linspace(20, 35, 30)
sales = 50 + 2 * temp + np.random.normal(0, 5, 30)
plt.figure(figsize=(8, 6))
plt.scatter(temp, sales)
plt.title('Temperature vs. Ice Cream Sales')
plt.xlabel('Temperature (°C)')
plt.ylabel('Sales ($)')
m, b = np.polyfit(temp, sales, 1)
plt.plot(temp, m*temp + b, color='red')
r = np.corrcoef(temp, sales)[0, 1]
print(f"Pearson's R: {r:.3f}")
plt.show()

# 4. Income Distribution Across Professions
np.random.seed(42)
engineers = np.random.exponential(80000, 100) + 40000
teachers = np.random.normal(55000, 8000, 100)
artists = np.random.lognormal(10.5, 0.4, 100)
plt.figure(figsize=(10, 6))
plt.boxplot([engineers, teachers, artists], labels=['Engineers', 'Teachers', 'Artists'])
plt.title('Income Distribution Across Professions')
plt.ylabel('Annual Income ($)')
plt.show()

# 5. Study Hours vs. Exam Scores Regression
np.random.seed(42)
hours = np.random.uniform(1, 10, 50)
scores = 30 + 7 * hours + np.random.normal(0, 5, 50)
plt.figure(figsize=(8, 6))
plt.scatter(hours, scores)
m, b = np.polyfit(hours, scores, 1)
plt.plot(hours, m*hours + b, color='red')
residuals = scores - (m*hours + b)
ss_res = np.sum(residuals**2)
ss_tot = np.sum((scores - np.mean(scores))**2)
r_squared = 1 - (ss_res / ss_tot)
plt.title(f'Study Hours vs. Exam Scores (R² = {r_squared:.2f})')
plt.xlabel('Study Hours')
plt.ylabel('Exam Scores')
plt.show()

# 6. Website Traffic Analysis
np.random.seed(42)
traffic = np.random.poisson(lam=50, size=744)
plt.figure(figsize=(10, 6))
plt.hist(traffic, bins=20, edgecolor='black')
plt.title('Website Traffic Distribution')
plt.xlabel('Hourly Visits')
plt.ylabel('Frequency')
plt.show()
z_scores = (traffic - np.mean(traffic)) / np.std(traffic)
anomalies = traffic[z_scores > 3]
print(f"Anomalous traffic hours: {anomalies}")

# 7. Advertising Spend vs. Revenue
np.random.seed(42)
spend = np.linspace(1000, 10000, 12)
revenue = 5000 + 2.5 * spend + np.random.normal(0, 1000, 12)
plt.figure(figsize=(8, 6))
plt.scatter(spend, revenue)
plt.title('Advertising Spend vs. Revenue')
plt.xlabel('Ad Spend ($)')
plt.ylabel('Revenue ($)')
m, b = np.polyfit(spend, revenue, 1)
plt.plot(spend, m*spend + b, color='red')
r, p = pearsonr(spend, revenue)
plt.annotate(f'Pearson\'s R = {r:.3f}\np-value = {p:.4f}', xy=(0.5, 0.1), xycoords='axes fraction')
plt.show()

# 8. Movie Genre Popularity
genres = ['Action', 'Comedy', 'Drama', 'Horror', 'Sci-Fi', 'Romance']
tickets = np.random.randint(5000, 30000, size=6)
min_idx = np.argmin(tickets)
explode = [0.1 if i == min_idx else 0 for i in range(len(genres))]
plt.figure(figsize=(8, 8))
plt.pie(tickets, labels=genres, explode=explode, autopct='%1.1f%%')
plt.title('Movie Genre Popularity')
plt.show()

# 9. Housing Price Analysis
np.random.seed(42)
suburban = np.random.normal(350000, 50000, 100)
urban = np.random.lognormal(12.8, 0.3, 100)
rural = np.random.exponential(250000, 100) + 150000
plt.figure(figsize=(10, 6))
plt.boxplot([suburban, urban, rural], labels=['Suburban', 'Urban', 'Rural'])
plt.title('Housing Price Distribution by Neighborhood')
plt.ylabel('Price ($)')
plt.show()
print(f"Suburban - Median: {np.median(suburban):.2f}, IQR: {np.percentile(suburban, 75) - np.percentile(suburban, 25):.2f}")
print(f"Urban - Median: {np.median(urban):.2f}, IQR: {np.percentile(urban, 75) - np.percentile(urban, 25):.2f}")
print(f"Rural - Median: {np.median(rural):.2f}, IQR: {np.percentile(rural, 75) - np.percentile(rural, 25):.2f}")

# 10. Athlete Performance: Age vs. Speed
np.random.seed(42)
age = np.random.randint(18, 40, 40)
speed = 10 - 0.15 * age + np.random.normal(0, 0.5, 40)
plt.figure(figsize=(8, 6))
plt.scatter(age, speed)
plt.title('Age vs. Sprint Speed')
plt.xlabel('Age (years)')
plt.ylabel('Speed (m/s)')
m, b = np.polyfit(age, speed, 1)
plt.plot(age, m*age + b, color='red')
r = np.corrcoef(age, speed)[0, 1]
print(f"Pearson's R: {r:.3f} (Negative correlation between age and speed)")
plt.show()