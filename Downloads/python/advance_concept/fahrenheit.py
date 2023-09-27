# List of Fahrenheit temperatures
temperatures = [75, 90, 60, 95, 40, 55, 70, 32, 100]

filtered_temperatures = filter(lambda x: 32 <= x <= 80, temperatures)

# Percentage
total_temperatures = len(temperatures)
filtered_count = len(list(filtered_temperatures))
percentage_within_range = (filtered_count / total_temperatures) * 100

print(f"Percentage of temperatures within the range 32 to 80: {percentage_within_range:.2f}%")