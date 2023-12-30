import os, string, time

printing = ""
printin = ""

i = 0


def cc():
    os.system('cls' if os.name == 'nt'
            else 'clear')


cc()
toprint = str(input("Gimme something to print!: "))


for i in range(len(toprint)):
    chartoget = toprint[i]
    #print(f"INDEX: {i}   CHARTOGET: {chartoget}")
    if chartoget == " ":
       printin = f"{printin} "
       time.sleep(0.05)
       cc()
       print(printin)
       continue
    elif chartoget.islower():  charset = string.ascii_lowercase
    elif chartoget.isupper():    charset = string.ascii_uppercase
    else: charset = "0123456789,.!?@#$%^&*"

    for u in range(len(charset)):
        time.sleep(0.05)
        cc()
        var = charset[u]
        printing = f"{printin}{var}"
        print(printing)
        #print(u+1)
        #print(len(charset))
        if var == chartoget:
            printin = printing
            break
        elif u+1 == len(charset):
            printin = f"{printin}?"
            break
#print(f"LINE TO GET: {toprint}") 
