# Napisati program koji učitava masu u kg i visinu u cm i stampa indeks tjelesne mase osobe.
# Koristi se sljedeća formula: (tjelesna masa u kg)/(visina u m)²


masa_kg = float(input("Unesite masu u kilogramima: "))

visina_cm = float(input("Unesite visinu u centimetrima: "))

visina_m = visina_cm / 100

bmi = masa_kg / (visina_m ** 2)

print("Indeks tjelesne mase (BMI) osobe je:", round(bmi, 2))
