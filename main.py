import numpy as np
import matplotlib.pyplot as plt

# Insights Section
def display_insights(mean, std_dev):
    print(f"Normal Distribution Insights:")
    print(f"1. Mean (μ): {mean}")
    print(f"2. Standard Deviation (σ): {std_dev}")
    print(f"3. The curve is symmetric around the mean.")
    print(f"4. Approximately 68% of the data lies within 1 standard deviation from the mean.")
    print(f"5. Approximately 95% of the data lies within 2 standard deviations from the mean.")
    print(f"6. Approximately 99.7% of the data lies within 3 standard deviations from the mean.")
    print(f"7. The area under the curve is 1, representing the total probability.")

# Parameters for the normal distribution
mean = 0   # Mean (average)
std_dev = 1  # Standard deviation

# Generate data points for the normal distribution
x = np.linspace(mean - 4*std_dev, mean + 4*std_dev, 1000)  # Range of x values
y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev)**2)  # Normal distribution formula

# Plot the normal distribution
plt.plot(x, y, label=f'Normal Distribution\nMean={mean}, Std Dev={std_dev}', color='blue')
plt.title('Normal Distribution')
plt.xlabel('X-axis')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()

# Display Insights
display_insights(mean, std_dev)
