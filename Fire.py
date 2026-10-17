import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')
df = df.dropna()
print(df.head())
print(df.info())

sns.barplot(x = 'day', y = 'total_bill', hue = 'sex', data = df)
plt.title('Total Bill per Day by Sex')
plt.xlabel('Day')
plt.ylabel('Average bill ($)')
plt.show()

sns.countplot(x = 'day', hue = 'sex', data = df)
plt.title('Count of Diners per Day by Sex')
plt.xlabel('Day')
plt.ylabel('Count')
plt.show()

sns.boxplot(x = 'day', y = 'total_bill', data = df)
plt.title('Spread of total Bill per day')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.stripplot(x = 'day', y = 'total_bill', data = df, jitter = True)
plt.title('Every bill amount per day (Stripplot)')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.swarmplot(x = 'day', y = 'tip', data = df)
plt.title('Every bill amount per day (Swarmplot)')
plt.xlabel('Day')
plt.ylabel('Total Bill ($)')
plt.show()

sns.jointplot(x = 'total_bill', y = 'tip', data = df)
plt.suptitle('Jointplot of Total Bill and Tip', y=1.02)
plt.show()

sns.jointplot(x = 'total_bill', y = 'tip', data = df, kind = 'kde')
plt.suptitle('Jointplot of Total Bill and Tip (KDE)', y=1.02)
plt.show()

sns.pairplot(df[['total_bill', 'tip', 'size']])
plt.suptitle('Pairplot of Total Bill, Tip and Size', y=1.02)
plt.show()

sns.pointplot(x = 'day', y = 'total_bill', hue = 'sex', data = df)
plt.title('Pointplot of Total Bill per Day by Sex')
plt.xlabel('Day')
plt.ylabel('Average bill ($)')
plt.show()

sns.lmplot(x = 'total_bill', y = 'tip', data = df)
plt.title('Total bill vs Tip (Trend line)')
plt.show()