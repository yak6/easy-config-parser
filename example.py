import loader

money = 300
xp = 1000

while True:
    loader.replace("money", money, "data.anything")
    loader.replace("xp", xp, "data.anything")
    choice = input("> ")
    if choice == "addmoney":
        money+=300
    elif choice == "addxp":
        xp+=300
    elif choice == "loadmoney":
        print(loader.load("money", "data.anything"))
    elif choice == "loadxp":
        print(loader.load("xp", "data.anything"))
