# ik wil een quiz schrijven die tegen je terug kan praten.

print("Hallo wat is je naam?")
name = input("Schrijf hier je naam ")

print("welkom " + name)
start_quiz = input ("Wil je een quiz maken " + name + "? ")

if start_quiz == "ja":
    print("Mooi zo laten we beginnen")

    eerste_vraag = input("vind je ict leuk? ")
    if eerste_vraag == "ja":
        print("Top ik ook")

    else: 
        print("Ik vindt je ook niet leuk")

    tweede_vraag = input("Vindt je je klas leuk? ")
    if tweede_vraag == "ja":
        print("ik vindt het ook een leuke klas")

    else:
        print("Onze klas vindt je ook niet leuk")  

    derde_vraag = input("Geven de docenten goed les op school? ") 
    if derde_vraag == "ja":
        print("Ik vindt ook dat ze goed les geven") 

    else:
        print("Dan luister je slecht want ze geven goed les")  

    laatste_vraag = input("Ga je je diploma van Software Developer halen? ")
    if laatste_vraag == "ja":
        print("Ik denk ook dat je het gaat halen") 

    else:
        print("Doe je best en dan haal je het wel")
















else: 
    print("Oke dan niet")



