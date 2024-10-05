list1 = ["Andrii Bojarin", "Aleksandr Zaschov", "Yurii Shukov"]
list2 = ["Vitalii Dudko", "Andrii Dudko", "Katerina Ebanova"]
list3 = ["Andrii Bojarov", "OLga Sikorova", "Lena Zashkovskaia"]

list4 = []
list6=[]

list5 = list1 + list2 + list3
for i in list5:
    a=i.split(" ")
    list4.append(a)

for i in list4:
    i.pop(1)
    list6.append(str(i))

n=list6.count("['Andrii']")

print(n)