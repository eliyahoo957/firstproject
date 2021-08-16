print("this is the market:\n--------\ntomato:3$\ncucumber:2$\nkola:5$\nchicken:20$\n\n")
tom = int(input("how much tomato? "))
cucu = int(input("how much cucumber? "))
ko = int(input("how much kola? "))
chi = int(input("how much chicken? "))
print("\n\nthis what you choose\ntomato: " + str(tom) + "\ncucumber: "+str(cucu)+"\nkola: "+str(ko)+"\nchicken: "+str(chi))

sum1 = 3*tom
sum2 = 2*cucu
sum3 = 5*ko
sum4 = 20*chi
summri = sum1+sum2+sum3 + sum4

print("\n\nyou need to pay withuot tax: " + str(summri))
print("\n\nyou need to pay with tax: " + str("%.2f" % (summri*1.17)))
