list1 = ["bilgisayar","uçak","araba","ev"]
list2 = ["ev","mouse","gelin","uçak"]
ortaklist = []


for ortak in list1:
    if ortak in list2:
        ortaklist.append(ortak)


print("Liste 1:",list1)
print("Liste 2:",list2)
print("\nOrtak Liste:",ortaklist)