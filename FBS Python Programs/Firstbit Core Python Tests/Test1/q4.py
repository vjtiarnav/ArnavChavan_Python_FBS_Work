s = float(input("Enter side length of each square: "))
ext_cost = float(input("Enter exterior wall cost per unit area: "))
int_cost = float(input("Enter interior wall cost per unit area: "))

exterior_area = 7 * s
interior_area = s

exterior_cost = exterior_area * ext_cost
interior_cost = interior_area * int_cost

total_cost = exterior_cost + interior_cost

print(f"Exterior wall area: {exterior_area}")
print(f"Interior wall area: {interior_area}")
print(f"Total painting cost: {total_cost}")