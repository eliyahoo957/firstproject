#LISTS
dettail = """eliyahoo nagari
19 years old
refaeliyahoo@gmail.com
0522064876"""
print("my full details:\n" + dettail + "\n\n----\n")

ip_a = ["111.111.111.111" ,"222.222.222.222"]
print("this is my ips: " + str(ip_a))

ip_a.append("333.333.333.333")
ip_a.append("2.2.2.2")
ip_a.append("1.1.1.1")
print("and this is ip's + 3 ip: " + str(ip_a))

ip_a.pop(2)
print("now ip's without the tree: " + str(ip_a) + "\nand you have in total: " + str(len(ip_a)) + " cells")
