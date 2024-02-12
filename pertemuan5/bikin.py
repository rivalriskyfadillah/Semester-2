print("\npenggunaan break pada looping")
print("--------------\n")
a = 0
b = float(input("masukan angka anda : "))
while a < b: # a < b adalah syarat
    a += 1 # INCREMENT
    if a == 5: # seleksi kondisi
        continue # continue point
    print(a)
     