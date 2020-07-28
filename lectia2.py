print("Bine ai venit la lectia a doua")
print("EXERCITIUL 1")
a=10
a+=len(str(a))
a=str(a)
print("Valoare lui 'a' este: ", a)

print("EXERCITIUL 2")
f=2
print(f"In padurea cu alune aveau casa {f} pitici")


print("EXERCITIUL 3")
a=10
a+1
print("Valoare este: ", a)

print("EXERCITIUL 4")
c = input("Scrie ceva:   ")
c =+ 1
print(c)


print("EXERCITIUL 5")
intro = input("Scoatem extensia la fisier:   ")
c = intro.split(".")
print(c[1])

print("EXERCITIUL 6")
a =['a','b','c','d']
a[int('3'*2)//11]
print("d")
a.insert(0,'r')
a.remove('d')
a.remove('c')
a.sort(reverse=True)
w=a.copy()
print("a = ",a)
print("w = ",w)

print("EXERCITIUL 7")

d={'scaune': 33, 'mese':44}
rezultat=sum(d.values())
print("Total eventarier: ", rezultat)