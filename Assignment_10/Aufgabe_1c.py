def calculate_overall_price_wrong(area, pps=40, tax=0.15):
    net = area * pps
    gross = net * tax
    return gross

def calculate_overall_price_correct(area, pps=40, tax=0.15):
    net = area * pps
    gross = net * (1 + tax)
    return gross

area = 500
pps = 85
expected = 500 * 85 * 1.15

print(f"{calculate_overall_price_wrong(area, pps) = :.0f}")
print(f"{expected = :.0f}")
print(f"{calculate_overall_price_correct(area, pps) = :.0f}")
