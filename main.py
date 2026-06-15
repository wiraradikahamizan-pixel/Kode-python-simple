import time

nama = input("Nama: ")
umur = int(input("Umur: "))

print("=== DATA ===")
print("Nama:", nama)

if umur >= 17:
    print("Status: Dewasa")
    print("mengirakan...")
    time.sleep(5)
    print("Dapet KTP")
else:
    print("Status: Bocil")
    print("mengirakan...")
    time.sleep(5)
    print("Ga dapet KTP")
