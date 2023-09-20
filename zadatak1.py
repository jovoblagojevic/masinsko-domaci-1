# Napisati program koji učitava dužinu stranice kvadrata i štampa njegov
# obim, površinu i dužinu dijagonale.
# Napomena: učitava se sa float(input('Unesite broj')).

while True:
    side = input("Unesite duzinu stranice: ")

    if side.strip() == "":
        print("Vrijednost za duzinu stranice ne smije biti prazna")
        continue

    try:
        side = float(side)
        if side > 0:
            print(f"Stranica: {side}")
            break
        else:
            print("Vrijednost za duzinu stranice nije pozitivan broj")
    except ValueError:
        print("Unesena vrijednost nije broj.")

print('**********************')
print('Proracun za kvadrat:')
print('**********************')
print('- Obim:', 4 * side)
print('- Povrsina:', side ** 2)
print(f'- Diagonala: {side * 2 ** 0.5:.2f}')
print('**********************')