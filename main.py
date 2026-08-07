from economy import Economy

economy = Economy()

economy.distribute_income()

print("Total income:", economy.calculate_total_income())
print("Consumption:", economy.calculate_consumption())