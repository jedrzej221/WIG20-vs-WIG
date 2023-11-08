import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style for better-looking graphs
sns.set(style='whitegrid')

# Define the ticker symbols
wig20_symbol = '^WIG20'  # WIG-20 index
wig_symbol = '^WIG'  # WIG index

# Download historical data
wig20_data = yf.download(wig20_symbol, start='2013-11-05', end='2023-11-05')
wig_data = yf.download(wig_symbol, start='2013-11-05', end='2023-11-05')

# Calculate daily returns
wig20_data['WIG_20_Returns'] = wig20_data['Adj Close'].pct_change() * 100
wig_data['WIG_Returns'] = wig_data['Adj Close'].pct_change() * 100

# Statistical analysis
correlation = wig_data['WIG_Returns'].corr(wig20_data['WIG_20_Returns'])
mean_wig_returns = wig_data['WIG_Returns'].mean()
mean_wig20_returns = wig20_data['WIG_20_Returns'].mean()

# Data Visualization
plt.figure(figsize=(12, 8))

# Time series plots with scatter lines for both indices
plt.subplot(2, 1, 1)
plt.scatter(wig_data.index, wig_data['WIG_Returns'], label='WIG Index', color='blue', marker='o', s=10)
plt.scatter(wig20_data.index, wig20_data['WIG_20_Returns'], label='WIG-20 Index', color='green', marker='x', s=10)
plt.title('Daily Returns Over Time')
plt.xlabel('Date')
plt.ylabel('Daily Returns (%)')
plt.legend()

# Box plots
plt.subplot(2, 1, 2)
sns.boxplot(data=[wig_data['WIG_Returns'], wig20_data['WIG_20_Returns']], palette=['blue', 'green'])
plt.title('Box Plot of Daily Returns')
plt.ylabel('Daily Returns (%)')

plt.tight_layout()
plt.show()

# Print statistical results
print(f"Correlation between WIG and WIG-20: {correlation:.2f}")
print(f"Mean daily returns for WIG: {mean_wig_returns:.2f}%")
print(f"Mean daily returns for WIG-20 Index: {mean_wig20_returns:.2f}%")
