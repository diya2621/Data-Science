#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
matplotlib.use('TkAgg')  # Opens plots in a separate window

# 1. Create the data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Covid_Cases': [5000, 15000, 30000, 25000, 20000, 10000],
    'Recoveries': [1000, 8000, 20000, 22000, 18000, 9500],
    'Beds_Used': [3000, 9000, 15000, 14000, 10000, 6000]
}

# Convert dictionary to a DataFrame (table)
df = pd.DataFrame(data)

# 2. Calculate active cases
df['Active_Cases'] = df['Covid_Cases'] - df['Recoveries']

# 3. Print the data
print("COVID-19 Health Data:\n")
print(df)

# 4. Set up the plot layout
sns.set(style='whitegrid')  # Clean background
fig, axs = plt.subplots(2, 2, figsize=(14, 10))  # 2 rows, 2 columns

# 5. Line chart: Cases vs Recoveries
axs[0, 0].plot(df['Month'], df['Covid_Cases'], marker='o', color='red', label='Covid Cases')
axs[0, 0].plot(df['Month'], df['Recoveries'], marker='o', color='green', label='Recoveries')
axs[0, 0].set_title('Cases vs Recoveries')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Number of People')
axs[0, 0].legend()

# 6. Bar chart: Beds Used
sns.barplot(x='Month', y='Beds_Used', data=df, palette='Blues', ax=axs[0, 1])
axs[0, 1].set_title('Hospital Beds Used')
axs[0, 1].set_xlabel('Month')
axs[0, 1].set_ylabel('Beds Used')

# 7. Bar chart: Active Cases
axs[1, 0].bar(df['Month'], df['Active_Cases'], color='orange')
axs[1, 0].set_title('Active COVID-19 Cases')
axs[1, 0].set_xlabel('Month')
axs[1, 0].set_ylabel('Active Cases')

# 8. Text summary in last subplot
axs[1, 1].axis('off')  # Hide chart border
text = df.to_string(index=False)
axs[1, 1].text(0.01, 1, "Data Summary:\n" + text, fontsize=10, fontfamily='monospace', verticalalignment='top')

# 9. Adjust layout and show all plots
plt.tight_layout()
plt.suptitle("COVID-19 Dashboard", fontsize=16, y=1.02)
plt.subplots_adjust(top=0.92)
plt.show()


# In[ ]:




