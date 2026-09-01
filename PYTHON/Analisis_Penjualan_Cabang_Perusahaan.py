penjualan = (
    ("Bandung", 120, 15000000),
    ("Jakarta", 200, 28000000),
    ("Surabaya", 150, 20000000),
    ("Medan", 100, 12000000)
)

total_revenue = 0
revenue_terbesar = 0
kota_terbesar = ""

for kota, item, revenue in penjualan:

    print(f"{kota} - {item} - Rp{revenue:,.0f}")

    total_revenue += revenue

    if revenue > revenue_terbesar:
        revenue_terbesar = revenue
        kota_terbesar = kota

print(f"\nTotal Revenue : Rp{total_revenue:,.0f}")
print(f"Kota dengan revenue terbesar : {kota_terbesar} - Rp{revenue_terbesar:,.0f}")