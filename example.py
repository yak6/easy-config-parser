import loader

money = 300
xp = 1000

while True:
    loader.replace("money", money, "data.as")
    loader.replace("xp", xp, "data.as")
    choice = input("> ")
    if choice == "addmoney":
        money+=300
    elif choice == "addxp":
        xp+=300
    elif choice == "loadmoney":
        print(loader.load("money", "data.as"))
    elif choice == "loadxp":
        print(loader.load("xp", "data.as"))