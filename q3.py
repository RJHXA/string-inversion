import json

with open('faturamento.json', 'r') as file:
    data = json.load(file)

daily_revenue = data["faturamento_diario"]

revenue = [day['valor'] for day in daily_revenue if day['valor'] > 0]

min_revenue = min(revenue)
max_revenue = max(revenue)

monthly_average = sum(revenue) / len(revenue)

days_above_average = sum(1 for value in revenue if value > monthly_average)

print(f"Minimum revenue: {min_revenue:.2f}")
print(f"Maximum revenue: {max_revenue:.2f}")
print(f"Number of days with revenue above the average: {days_above_average}")