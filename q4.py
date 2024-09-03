state_revenue = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Others": 19849.53
}

total_revenue = sum(state_revenue.values())

print("Percentage representation by state:")
for state, revenue in state_revenue.items():
    percentage = (revenue / total_revenue) * 100
    print(f"{state}: {percentage:.2f}%")
