mapel = ("matematika","ddj","olahraga","jepang")

mapel_list =(mapel)
print("tuple =",mapel)
print("list = ",mapel_list)
mapel_list.append("english")
mapel_list[0] = "informatika"
del mapel_list [2]
print (mapel_list)
mapel_tuple = tuple(mapel_list)
print(mapel_tuple)