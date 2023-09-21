#  Petar je u školu donio korpu sa a jabuka iz svoje bašte.
#  Podijelio je jabuke drugarima iz odjeljenja, tako da je svako od  b drugara
#  dobio najveći mogući broj jabuka i svi su dobili isti broj jabuka.
#  Preostale jabuke iz korpe odnio je portiru Marku.
#  Napisati program koji učitava dva cijela broja a i b  i štampa dva broja:
#  koliko je svaki od drugara dobio jabuka i koliko je jabuka dobio portir.
#  Koristite operator % - ostatak pri dijeljenju

a = int(input('Unesite broj jabuka  koje je Petar donio iz bašte: '))
b = int(input('Unesite broj drugara iz odjeljenja: '))

jabuke_po_drugaru = a // b
ostatak_jabuka = a % b

print("Svaki drugar je dobio", jabuke_po_drugaru, "jabuka.")
print("Portir Marko je dobio", ostatak_jabuka, "jabuka.")