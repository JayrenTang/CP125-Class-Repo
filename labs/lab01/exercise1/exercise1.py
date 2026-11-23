def is_budget_sufficient(one_way_km, budget):
    litre = (one_way_km / 10) * 2 
    cost = litre * 2

    if cost <= budget:
        return True
    else:
        return False

print(is_budget_sufficient(100, 40))
print(is_budget_sufficient(100, 39))