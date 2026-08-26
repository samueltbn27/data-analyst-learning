sales = 8500000
target = 10000000
cost = 5000000

profit = sales - cost

profit_margin = (profit / sales) * 100

if sales >= target * 0.8 and profit_margin >= 30:
    kondisi = "Performance Baik"
else:
    kondisi = "Performance Perlu Evaluasi"

print(f"Profit : {profit:,.2f}")
print(f"Profit Margin : {profit_margin:.2f}%")
print(f"Status : {kondisi}")