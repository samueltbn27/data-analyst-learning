monthly_sales = 27500000
sales_target = 30000000
customer_visits = 1250
transactions = 980
customer_complaints = 18

target_achievement = (monthly_sales / sales_target) * 100

conversion_rate = (transactions / customer_visits) * 100

if target_achievement >= 90 and conversion_rate >= 75 and customer_complaints <= 20:
    kondisi = "Layak Mendapat Bonus"

elif target_achievement >= 80 and conversion_rate >= 65 and customer_complaints <= 30:
    kondisi = "Perlu Evaluasi"

else:
    kondisi = "Tidak Layak Mendapat Bonus"

print(f"Monthly Sales : {monthly_sales}")
print(f"Target Achievement : {target_achievement:.2f}%")
print(f"Conversion Rate : {conversion_rate:.2f}%")
print(f"Customer Complaints : {customer_complaints}")
print(f"Status : {kondisi}")