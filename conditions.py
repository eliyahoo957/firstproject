menu = input(str(
    "menu:\n\n1.insert a number.\n2.insert 4 ips.\n3.insert 4 DNS with their ips.\n4.checking.\n\nplease choose 1-4:\n"))
if menu == "1":
    print("the number **3 :" + str(int(input("insert a number: ")) ** 3))

elif menu == "2":
    list_ip = [input("insert ip:\n"), input("insert ip:\n"), input("insert ip:\n"), input("insert ip:\n")]
    print("this is your ips list:\n------\n" + str(list_ip))

elif menu == "3":
    dns_dict = {input("insert DNS: "): input("insert ip") , input("insert DNS: "): input("insert ip") , input("insert DNS: "): input("insert ip") ,input("insert DNS: "): input("insert ip")}
    print("this is your DNS_dict: \n" + str(dns_dict))

elif menu == "4":
    word = input("coise a word: ")
    if word == word[::-1]:
        print("this word is polindrom")
    else:
        print("the word isn't polindrom")
else:
    print(str("please choose 1-4 only."))
