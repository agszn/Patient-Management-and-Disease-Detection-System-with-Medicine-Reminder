import seaborn as sns
import matplotlib.pyplot as plt

# Sample data - number of medicines consumed by the patient for each week of the month
weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
medicines_consumed = [10, 8, 12, 9]  # Sample data, you can replace this with your actual data

# Set the style
sns.set_style("whitegrid")

# Plotting the bar graph using Seaborn
plt.figure(figsize=(10, 6))
sns.barplot(x=weeks, y=medicines_consumed, palette="Blues_d")

# Adding title and labels
plt.title('Medicines Consumed by Patient Each Week')
plt.xlabel('Week of the Month')
plt.ylabel('Number of Medicines Consumed')

# Adding the value labels on top of each bar
for i in range(len(weeks)):
    plt.text(i, medicines_consumed[i], str(medicines_consumed[i]), ha='center', va='bottom')

# Displaying the plot
plt.tight_layout()
plt.show()
