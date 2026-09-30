airtimebalance = 10
databalance = "700mb"
choice = input("Welcome to MTN, dail code \n:")
if choice == "*312#":
 code = input(" 1.Buy data\n 2.Gift data\n 3.Share data\n 4.Check data balance\n 5.Voice plan\n 6.MySpcl offer\n 7.Magic data bundle\n:")
 if code == "1":
    code = input(" 1. Proceed(Auto renew)\n 2. Proceed(One off)\n 99. Back\n 0. Exit\n\n:")
 elif code == "2":
    code = input(" 1. Daily - weekly plans\n 2. Monthly data\n 3. Mega data\n 4. Super mega data\n 5. Special data\n\n:")
 elif code == "3":
    code = input(" 11. Share data\n 2. Unshare data\n 3. List of shared numbers\n 4. Cancel auto renew\n 5. Manual configuration details\n 6. Easy share (credit share)\n 0. Exist\n\n:")
elif choice == "*310#":
    print("Your airtime balance", airtimebalance)
elif choice == "*323#":
    print("Your data balance", databalance)
else:
    print("Invalid")
