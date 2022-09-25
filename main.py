import random

elements = ['tas','kagit','makas']
pcscore = 0
humanscore = 0
while True:
    print("""
        Lütfen bir tanesini seçin.
        
        1) Taş
        2) Kağıt
        3) Makas
        
        """)
    human = int(input("> "))

    pc = random.choice(elements)

    if human==1 and pc=='tas':
        print("Berabere.")

    if human==1 and pc=='kagit':
        print("Bilgisayar Kazandı.")
        pcscore = pcscore+1

    if human==1 and pc=='makas':
        print("Kazandın.")
        humanscore = humanscore+1

    if human==2 and pc=='tas':
        print("Kazandın.")
        humanscore = humanscore+1

    if human==2 and pc=='kagit':
        print("Berabere.")

    if human==2 and pc=='makas':
        print("Bilgisayar Kazandı.")
        pcscore = pcscore+1
        
    if human==3 and pc=='tas':
        print("Bilgisayar Kazandı.")
        pcscore = pcscore+1

    if human==3 and pc=='kagit':
        print("Kazandın.")
        humanscore = humanscore+1

    if human==3 and pc=='makas':
        print("Berabere.")
    else:
        print(humanscore,"-",pcscore)