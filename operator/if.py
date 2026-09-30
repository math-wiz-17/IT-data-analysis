airtimebalance = "30"
databalance = "700mb"

choice = input("Dail code \n:")

if choice == "*312#":
    code = input(" 1.Buy data\n 2.Gift data\n 3.Share data\n 4.Check data balance\n 5.Voice plan\n 6.MySpcl offer\n 7.Magic data bundle\n:")
    if code == "1":
        code = input(" 1. Proceed(Auto renew)\n 2. Proceed(One off)\n 99. Back\n 0. Exit\n\n:")

        if code == "1":
            code = input(" 1. 1GB - N350\n 2. 2GB - N600\n 3. 5GB - N1500\n 4. 10GB - N3000\n 0. Exit\n\n:")

            if code == "1":
                print("1GB purchased successfully")
            elif code == "2":
                print("2GB purchased successfully")
            elif code == "3":
                print("5GB purchased successfully")
            elif code == "4":
                print("10GB purchased successfully")
            elif code == "0":
                print("Exit")
            else:
                print("Invalid")
        elif code == "2":
            code = input(" 1. 1GB - N350\n 2. 2GB - N600\n 3. 5GB - N1500\n 4. 10GB - N3000\n 0. Exit\n\n:")
            if code == "1":
                print("1GB purchased successfully")
            elif code == "2":
                print("2GB purchased successfully")
            elif code == "3":
                print("5GB purchased successfully")
            elif code == "4":
                print("10GB purchased successfully")
            elif code == "0":
                print("Exit")
            else:
                print("Invalid")

        elif code == "99":
            print("Back")
        elif code == "0":
            print("Exit")
        else:
            print("Invalid")

    elif code == "2":
        code = input(" 1. Daily - weekly plans\n 2. Monthly data\n 3. Mega data\n 4. Super mega data\n 5. Special data\n 0. Exit\n\n:")

        if code == "1":
            print("Daily - weekly plans selected")
        elif code == "2":
            print("Monthly data selected")
        elif code == "3":
            print("Mega data selected")
        elif code == "4":
            print("Super mega data selected")
        elif code == "5":
            print("Special data selected")
        elif code == "0":
            print("Exit")
        else:
            print("Invalid")

    elif code == "3":
        code = input(" 1. Share data\n 2. Unshare data\n 3. List of shared numbers\n 4. Cancel auto renew\n 5. Manual configuration details\n 6. Easy share (credit share)\n 0. Exit\n\n:")

        if code == "1":
            print("Share data selected")
        elif code == "2":
            print("Unshare data selected")
        elif code == "3":
            print("List of shared numbers")
        elif code == "4":
            print("Auto renew cancelled")
        elif code == "5":
            print("Manual configuration details")
        elif code == "6":
            print("Easy share selected")
        elif code == "0":
            print("Exit")
        else:
            print("Invalid")

    elif code == "4":
        print("Your data balance", databalance)

    elif code == "5":
        code = input(" 1. Voice plans\n 2. Check voice balance\n 3. Other voice services\n 0. Exit\n\n:")

        if code == "1":
            print("Voice plans selected")
        elif code == "2":
            print("Your voice balance is 10 minutes")
        elif code == "3":
            print("Other voice services selected")
        elif code == "0":
            print("Exit")
        else:
            print("Invalid")

    elif code == "6":
        code = input(" 1. My special offer\n 2. Check offer\n 0. Exit\n\n:")

        if code == "1":
            print("My special offer selected")
        elif code == "2":
            print("Your special offer is available")
        elif code == "0":
            print("Exit")
        else:
            print("Invalid")
    elif code == "7":
        code = input(" 1. Magic data bundle\n 2. Check magic bundle\n 0. Exit\n\n:")
        if code == "1":
            print("Magic data bundle selected")
        elif code == "2":
            print("Your magic data bundle is available")
        elif code == "0":
            print("Exit")
        else:
            print("Invalid")
    else:
        print("Invalid")
elif choice == "*310#":
    print("Your airtime balance", airtimebalance)
elif choice == "*323#":
    print("Your data balance", databalance)
else:
    print("Invalid")