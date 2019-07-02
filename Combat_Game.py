import random

# Battle begins.
print("Welcome to the Battle Arena")

# Catches any kind of exception and prints stacktrace while asking user to restart the game.
try:

    while True:
        # Catches ValueError exception and prints stacktrace.
        try:
            # Mode is set to 1 if player likes to play with another or set to 2 if he wants to play with computer.
            mode = int(
                input("For starting game with Player Vs Player mode press 1 and for Player Vs Computer mode press 2."))
            if mode != 1 and mode != 2:
                continue
            break
        except ValueError as e:
            print("Please enter only numbers.", e)
    print("Rules :\n1. Each Commander has been given $10.")
    print("2. Costs,\nArcher : $1\nSoldier : $1.5\nKnight : $2\nSiege Equipment : $1.75\nWizard : $2.5")
    print("3. Commanders can select a max of $10 army.")

    # If players chose to play with each other.
    if mode == 1:
        # Commander 1 selects his army.
        print("Commander 1 please select your team.")

        # Continuous looping until commander 1 makes the right selection.
        while True:
            # Catches ValueError exception and prints stacktrace.
            try:
                # Ask commander 1 to make a choice as a string with comma separated.
                comm1_resp = str(
                    input("Press the numbers separated by commas as \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n"))
                # Converting string to list of values.
                comm1_List = list(map(int, comm1_resp.split(',')))
                e_sum = 0 # Variable initialization to calculate value of army selected by commander 1.
                for e in comm1_List:
                    if e == 1:
                        e_sum = e_sum + 1
                    elif e == 2:
                        e_sum = e_sum + 1.5
                    elif e == 3:
                        e_sum = e_sum + 2
                    elif e == 4:
                        e_sum = e_sum + 1.75
                    elif e == 5:
                        e_sum = e_sum + 2.5
                a = 0
                while True:
                    # Prompt if commander 1 has any funds left.
                    if e_sum < 10 and 10 - e_sum > 1:
                        print("Commander 1, you have selected only $", e_sum,"worth of your army.")
                        while True:
                            # Catches ValueError exception and prints stacktrace.
                            try:
                                yesNo = int(input("Do you want to select more? If Yes, press 1 or else 0"))
                                break
                            except ValueError as e:
                                print("Please enter only numbers.",e)
                        # Commader 1 makes selection of army for remaining funds
                        if yesNo == 1:
                            while True:
                                print("Commander 1, please select another $", 10 - e_sum, "of your army.")
                                comm1_respExt = input(
                                    "Enter the numbers separated by coma \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n")
                                comm1_ListExt = list(map(int, comm1_respExt.split(',')))
                                # Variable initialization to calculate remaining value of army selected by commander 1.
                                e_sumExt = 0
                                for e in comm1_ListExt:
                                    if e == 1:
                                        e_sumExt = e_sumExt + 1
                                    elif e == 2:
                                        e_sumExt = e_sumExt + 1.5
                                    elif e == 3:
                                        e_sumExt = e_sumExt + 2
                                    elif e == 4:
                                        e_sumExt = e_sumExt + 1.75
                                    elif e == 5:
                                        e_sumExt = e_sumExt + 2.5

                                if e_sumExt + e_sum <= 10:
                                    for x in comm1_ListExt:
                                        comm1_List.append(x)
                                    break
                                else:
                                    continue
                            e_sum = 0
                            # Sum re-calculation for accuracy
                            for e in comm1_List:
                                if e == 1:
                                    e_sum = e_sum + 1
                                elif e == 2:
                                    e_sum = e_sum + 1.5
                                elif e == 3:
                                    e_sum = e_sum + 2
                                elif e == 4:
                                    e_sum = e_sum + 1.75
                                elif e == 5:
                                    e_sum = e_sum + 2.5

                    # If selected army worth is more than $10.
                    while True:
                        if e_sum > 10:
                            print("Commander 1 please select a maximum of $10 army.")
                            comm1_resp = input(
                                "Press the numbers separated by commas as \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n")
                            comm1_List = list(map(int, comm1_resp.split(',')))
                            e_sum = 0
                            for e in comm1_List:
                                if e == 1:
                                    e_sum = e_sum + 1
                                elif e == 2:
                                    e_sum = e_sum + 1.5
                                elif e == 3:
                                    e_sum = e_sum + 2
                                elif e == 4:
                                    e_sum = e_sum + 1.75
                                elif e == 5:
                                    e_sum = e_sum + 2.5
                            a = 1
                        else:
                            break
                    # Prompts error and selection resets if entered army is not in list.
                    if any(n not in range(1,6) for n in comm1_List):
                        print("Please select army numbers ranging from 1 to 5.")
                        print("Commander 1 please select a maximum of 10 army.")
                        comm1_resp = input(
                            "Press the numbers separated by commas as \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n")
                        comm1_List = list(map(int, comm1_resp.split(',')))

                        e_sum = 0
                        for e in comm1_List:
                            if e == 1:
                                e_sum = e_sum + 1
                            elif e == 2:
                                e_sum = e_sum + 1.5
                            elif e == 3:
                                e_sum = e_sum + 2
                            elif e == 4:
                                e_sum = e_sum + 1.75
                            elif e == 5:
                                e_sum = e_sum + 2.5

                        a = 1
                    else:
                        a = 0
                        break
                    if a == 0:
                        break
                    else:
                        continue
                break

            except ValueError as e:
                print("Please enter only numbers.",e)

        j = 0
        comm1_dict = {}

        # Adding commander 1 army to dictionary for health assignment.
        for i in comm1_List:
            j = j+1
            if i == 1:
                comm1_dict[str(i)+","+str(j)] = 1
            elif i == 2:
                comm1_dict[str(i)+"," + str(j)] = 2
            elif i == 3:
                comm1_dict[str(i)+"," + str(j)] = 3
            elif i == 4:
                comm1_dict[str(i)+"," + str(j)] = 4
            elif i == 5:
                comm1_dict[str(i)+"," + str(j)] = 5

        # Commander 2 selects his team.
        print("Commander 2 please select your team.")
        while True:
            # Catches ValueError exception and prints stacktrace.
            try:
                comm2_resp = input(
                    "Press the numbers separated by commas as \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n")
                comm2_List = list(map(int, comm2_resp.split(',')))

                e_sum = 0
                for e in comm2_List:
                    if e == 1:
                        e_sum = e_sum + 1
                    elif e == 2:
                        e_sum = e_sum + 1.5
                    elif e == 3:
                        e_sum = e_sum + 2
                    elif e == 4:
                        e_sum = e_sum + 1.75
                    elif e == 5:
                        e_sum = e_sum + 2.5

                a = 0
                while True:

                    if e_sum < 10 and 10 - e_sum > 1:
                        print("Commander 2, you have selected only", e_sum, "of your army.")
                        while True:
                            # Catches ValueError exception and prints stacktrace.
                            try:
                                yesNo = int(input("Do you want to select more? If Yes, press 1 or else 0"))
                                break
                            except ValueError as e:
                                print("Please enter only numbers.",e)
                        # Executes on commander decision. If 1 commander can select more army for remaining amount or else exit
                        if yesNo == 1:
                            while True:
                                print("Commander 2, please select another $", 10 - e_sum, "of your army.")
                                comm2_respExt = input(
                                    "Enter the numbers separated by comma \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n")
                                comm2_ListExt = list(map(int, comm2_respExt.split(',')))

                                e_sumExt = 0
                                for e in comm2_ListExt:
                                    if e == 1:
                                        e_sumExt = e_sumExt + 1
                                    elif e == 2:
                                        e_sumExt = e_sumExt + 1.5
                                    elif e == 3:
                                        e_sumExt = e_sumExt + 2
                                    elif e == 4:
                                        e_sumExt = e_sumExt + 1.75
                                    elif e == 5:
                                        e_sumExt = e_sumExt + 2.5

                                if e_sumExt + e_sum <= 10:
                                    for x in comm2_ListExt:
                                        comm2_List.append(x)
                                    break
                                else:
                                    continue
                            # Sum recalculation for final selected army.
                            e_sum = 0
                            for e in comm2_List:
                                if e == 1:
                                    e_sum = e_sum + 1
                                elif e == 2:
                                    e_sum = e_sum + 1.5
                                elif e == 3:
                                    e_sum = e_sum + 2
                                elif e == 4:
                                    e_sum = e_sum + 1.75
                                elif e == 5:
                                    e_sum = e_sum + 2.5

                    # Commander 2 selects army
                    while True:
                        if e_sum > 10:
                            print("Commander 2 please select a maximum of $10 army.")
                            comm2_resp = input(
                                "Press the numbers separated by commas as \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n")
                            comm2_List = list(map(int, comm2_resp.split(',')))
                            e_sum = 0
                            for e in comm2_List:
                                if e == 1:
                                    e_sum = e_sum + 1
                                elif e == 2:
                                    e_sum = e_sum + 1.5
                                elif e == 3:
                                    e_sum = e_sum + 2
                                elif e == 4:
                                    e_sum = e_sum + 1.75
                                elif e == 5:
                                    e_sum = e_sum + 2.5
                            a = 1
                        else:
                            break

                    # If any out of range number is entered.
                    if any(n not in range(1,6) for n in comm2_List):
                        print("Please select army numbers ranging from 1 to 5.")
                        print("Commander 2 please select a maximum of 10 army.")
                        comm2_resp = input(
                            "Press the numbers separated by commas as \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n")
                        comm2_List = list(map(int, comm2_resp.split(',')))

                        e_sum = 0
                        for e in comm2_List:
                            if e == 1:
                                e_sum = e_sum + 1
                            elif e == 2:
                                e_sum = e_sum + 1.5
                            elif e == 3:
                                e_sum = e_sum + 2
                            elif e == 4:
                                e_sum = e_sum + 1.75
                            elif e == 5:
                                e_sum = e_sum + 2.5

                        a = 1
                    else:
                        a = 0
                        break
                    if a == 0:
                        break
                    else:
                        continue
                break

            except ValueError as e:
                print("Please enter only numbers.",e)

        j = 0
        comm2_dict = {}

        for i in comm2_List:
            j = j + 1
            if i == 1:
                comm2_dict[str(i)+"," + str(j)] = 1
            elif i == 2:
                comm2_dict[str(i)+"," + str(j)] = 2
            elif i == 3:
                comm2_dict[str(i)+"," + str(j)] = 3
            elif i == 4:
                comm2_dict[str(i)+"," + str(j)] = 4
            elif i == 5:
                comm2_dict[str(i)+"," + str(j)] = 5

    # Mode 2 for AI Mode, which involves player Vs Computer
    elif mode == 2:
        print("Commander please select your team.")

        # Commander 1 selects his team
        while True:
            try:
                comm1_resp = str(
                    input("Press the numbers separated by commas as \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n"))
                comm1_List = list(map(int, comm1_resp.split(',')))
                e_sum = 0
                for e in comm1_List:
                    if e == 1:
                        e_sum = e_sum + 1
                    elif e == 2:
                        e_sum = e_sum + 1.5
                    elif e == 3:
                        e_sum = e_sum + 2
                    elif e == 4:
                        e_sum = e_sum + 1.75
                    elif e == 5:
                        e_sum = e_sum + 2.5
                a = 0
                # If commander 1 lefts with any balance for army selection.
                while True:
                    if e_sum < 10 and 10 - e_sum > 1:
                        print("Commander 1, you have selected only $",e_sum,"worth of your army.")
                        while True:
                            # Catches ValueError exception and prints stacktrace.
                            try:
                                yesNo = int(input("Do you want to select more? If Yes, press 1 or else 0"))
                                break
                            except ValueError as e:
                                print("Please enter only numbers.",e)

                        # If commander 1 is willing to select more army.
                        if yesNo == 1:
                            while True:
                                print("Commander 1, please select another $", 10 - e_sum, "of your army.")
                                comm1_respExt = input(
                                    "Enter the numbers separated by comma \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n")
                                comm1_ListExt = list(map(int, comm1_respExt.split(',')))

                                e_sumExt = 0
                                for e in comm1_ListExt:
                                    if e == 1:
                                        e_sumExt = e_sumExt + 1
                                    elif e == 2:
                                        e_sumExt = e_sumExt + 1.5
                                    elif e == 3:
                                        e_sumExt = e_sumExt + 2
                                    elif e == 4:
                                        e_sumExt = e_sumExt + 1.75
                                    elif e == 5:
                                        e_sumExt = e_sumExt + 2.5

                                if e_sumExt + e_sum <= 10:
                                    for x in comm1_ListExt:
                                        comm1_List.append(x)
                                    break
                                else:
                                    continue
                            e_sum = 0
                            for e in comm1_List:
                                if e == 1:
                                    e_sum = e_sum + 1
                                elif e == 2:
                                    e_sum = e_sum + 1.5
                                elif e == 3:
                                    e_sum = e_sum + 2
                                elif e == 4:
                                    e_sum = e_sum + 1.75
                                elif e == 5:
                                    e_sum = e_sum + 2.5
                            print("e_sum :", e_sum)

                    while True:
                        if e_sum > 10:
                            print("Commander 1 please select a maximum of $10 army.")
                            comm1_resp = input(
                                "Press the numbers separated by commas as \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n")
                            comm1_List = list(map(int, comm1_resp.split(',')))
                            e_sum = 0
                            for e in comm1_List:
                                if e == 1:
                                    e_sum = e_sum + 1
                                elif e == 2:
                                    e_sum = e_sum + 1.5
                                elif e == 3:
                                    e_sum = e_sum + 2
                                elif e == 4:
                                    e_sum = e_sum + 1.75
                                elif e == 5:
                                    e_sum = e_sum + 2.5
                            print("e_sum :", e_sum)
                            a = 1
                        else:
                            break

                    if any(n not in range(1,6) for n in comm1_List):
                        print("Please select army numbers ranging from 1 to 5.")
                        print("Commander 1 please select a maximum of 10 army.")
                        comm1_resp = input(
                            "Press the numbers separated by commas as \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard\n\n")
                        comm1_List = list(map(int, comm1_resp.split(',')))

                        e_sum = 0
                        for e in comm1_List:
                            if e == 1:
                                e_sum = e_sum + 1
                            elif e == 2:
                                e_sum = e_sum + 1.5
                            elif e == 3:
                                e_sum = e_sum + 2
                            elif e == 4:
                                e_sum = e_sum + 1.75
                            elif e == 5:
                                e_sum = e_sum + 2.5
                        print("e_sum :", e_sum)

                        a = 1
                    else:
                        a = 0
                        break
                    if a == 0:
                        break
                    else:
                        continue
                break

            except ValueError as e:
                print("Please enter only numbers.",e)

        j = 0
        comm1_dict = {}

        for i in comm1_List:
            j = j+1
            if i == 1:
                comm1_dict[str(i)+","+str(j)] = 1
            elif i == 2:
                comm1_dict[str(i)+"," + str(j)] = 2
            elif i == 3:
                comm1_dict[str(i)+"," + str(j)] = 3
            elif i == 4:
                comm1_dict[str(i)+"," + str(j)] = 4
            elif i == 5:
                comm1_dict[str(i)+"," + str(j)] = 5

        print("Please wait while Commander 2 computer is making selection.")
        comm2_List = []

        lim_var = 10.0
        i_list = []
        # Logic for AI to make its selection.
        while lim_var >= 0.0:
            i = int(random.choice([1.0, 1.5, 2.0, 1.75, 2.5]))
            i_list.append(i)
            if 10 - sum(i_list) not in [1.0, 1.5, 2.0, 1.75, 2.5] and 10 - sum(i_list) < 0.0:
                break
            if i == 1.0:
                comm2_List.append(1)
            elif i == 1.5:
                comm2_List.append(2)
            elif i == 2:
                comm2_List.append(3)
            elif i == 1.75:
                comm2_List.append(4)
            elif i == 2.5:
                comm2_List.append(5)
            lim_var = lim_var - 1

        print("Commander 2 computer selected :", comm2_List)
        print("Where numbers correspond to \n1 for Archer\n2 for Soldier\n3 for Knight \n4 for Siege Equipment \n5 for Wizard")

        j = 0
        comm2_dict = {}

        for i in comm2_List:
            j = j + 1
            if i == 1:
                comm2_dict[str(i) + "," + str(j)] = 1
            elif i == 2:
                comm2_dict[str(i) + "," + str(j)] = 2
            elif i == 3:
                comm2_dict[str(i) + "," + str(j)] = 3
            elif i == 4:
                comm2_dict[str(i) + "," + str(j)] = 4
            elif i == 5:
                comm2_dict[str(i) + "," + str(j)] = 5

    p = 0
    q = 0

    print("Commanders, please wait while you embrace for battle.")

    # Loop to enable wait time before battle begins.
    while i < 1000000:
        i += 1

    # Battle logic
    while True:
        while True:
            # Fight with Commander 1 Archer.

            if int(list(comm1_dict.keys())[p].split(",")[0]) == 1 and int(list(comm2_dict.keys())[q].split(",")[0]) == 1:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 2
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 2

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Archer and Commander 2 sends : Archer. It's a tie")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 1 and int(list(comm2_dict.keys())[q].split(",")[0]) == 2:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 1
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 3

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Archer and Commander 2 sends : Soldier. it's a Commander 1 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 1 and int(list(comm2_dict.keys())[q].split(",")[0]) == 3:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 3
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 1

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Archer and Commander 2 sends : Knight. it's a Commander 2 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 1 and int(list(comm2_dict.keys())[q].split(",")[0]) == 4:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 3
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 1

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Archer and Commander 2 sends : Siege Equipment. it's a Commander 2 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 1 and int(list(comm2_dict.keys())[q].split(",")[0]) == 5:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 1
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 3

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Archer and Commander 2 sends : Wizard. it's a Commander 1 Win")
                break

            # Fight with Commander 1 Soldier.

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 2 and int(list(comm2_dict.keys())[q].split(",")[0]) == 1:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 3
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 1

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Soldier and Commander 2 sends : Archer. it's a Commander 2 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 2 and int(list(comm2_dict.keys())[q].split(",")[0]) == 2:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 2
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 2

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Soldier and Commander 2 sends : Soldier. it's a tie")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 2 and int(list(comm2_dict.keys())[q].split(",")[0]) == 3:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 1
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 3

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Soldier and Commander 2 sends : Knight. it's a Commander 1 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 2 and int(list(comm2_dict.keys())[q].split(",")[0]) == 4:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 3
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 1

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Soldier and Commander 2 sends : Siege Equipment. it's a Commander 2 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 2 and int(list(comm2_dict.keys())[q].split(",")[0]) == 5:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 3
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 1

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Soldier and Commander 2 sends : Wizard. it's a Commander 2 Win")
                break

            # Fight with Commander 1 Knight.

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 3 and int(list(comm2_dict.keys())[q].split(",")[0]) == 1:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 1
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 3

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Knight and Commander 2 sends : Archer. it's a Commander 1 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 3 and int(list(comm2_dict.keys())[q].split(",")[0]) == 2:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 3
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 1

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Knight and Commander 2 sends : Soldier. it's a Commander 2 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 3 and int(list(comm2_dict.keys())[q].split(",")[0]) == 3:
                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 2
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 2

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Knight and Commander 2 sends : Knight. it's a tie")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 3 and int(list(comm2_dict.keys())[q].split(",")[0]) == 4:
                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 1
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 3

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Knight and Commander 2 sends : Siege Equipment. it's a Commander 1 win.")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 3 and int(list(comm2_dict.keys())[q].split(",")[0]) == 5:
                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 3
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 1

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Knight and Commander 2 sends : Wizard. it's a Commander 2 win.")
                break

            # Fight with Commander 1 Siege Equipment.

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 4 and int(list(comm2_dict.keys())[q].split(",")[0]) == 1:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 1
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 3

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Siege Equipment and Commander 2 sends : Archer. it's a Commander 1 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 4 and int(list(comm2_dict.keys())[q].split(",")[0]) == 2:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 1
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 3

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Siege Equipment and Commander 2 sends : Soldier. it's a Commander 1 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 4 and int(list(comm2_dict.keys())[q].split(",")[0]) == 3:
                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 3
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 1

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Siege Equipment and Commander 2 sends : Knight. it's a Commander 2 win.")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 4 and int(list(comm2_dict.keys())[q].split(",")[0]) == 4:
                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 2
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 2

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Siege Equipment and Commander 2 sends : Siege Equipment. it's a tie.")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 4 and int(list(comm2_dict.keys())[q].split(",")[0]) == 5:
                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 3
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 1

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Siege Equipment and Commander 2 sends : Wizard. it's a Commander 2 win.")
                break

            # Fight with Commander 1 Wizard

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 5 and int(list(comm2_dict.keys())[q].split(",")[0]) == 1:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 3
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 1

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Wizard and Commander 2 sends : Archer. it's a Commander 2 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 5 and int(list(comm2_dict.keys())[q].split(",")[0]) == 2:

                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 1
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 3

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Wizard and Commander 2 sends : Soldier. it's a Commander 1 Win")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 5 and int(list(comm2_dict.keys())[q].split(",")[0]) == 3:
                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 1
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 3

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Wizard and Commander 2 sends : Knight. it's a Commander 1 win.")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 5 and int(list(comm2_dict.keys())[q].split(",")[0]) == 4:
                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 1
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 3

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Wizard and Commander 2 sends : Siege Equipment. it's a Commander 1 win.")
                break

            elif int(list(comm1_dict.keys())[p].split(",")[0]) == 5 and int(list(comm2_dict.keys())[q].split(",")[0]) == 5:
                a = "".join(str(x) for x in list(comm1_dict.keys())[p])
                b = "".join(str(y) for y in list(comm2_dict.keys())[q])
                comm1_dict[list(comm1_dict.keys())[p]] = comm1_dict[a] - 2
                comm2_dict[list(comm2_dict.keys())[q]] = comm2_dict[b] - 2

                if comm1_dict[a] <= 0:
                    del comm1_dict[list(comm1_dict.keys())[p]]
                if comm2_dict[b] <= 0:
                    del comm2_dict[list(comm2_dict.keys())[q]]

                print("Commander 1 sends : Wizard and Commander 2 sends : Wizard. it's a tie.")
                break

        # If any of the commanders are out of army, the loop breaks.
        if len(comm1_dict) == 0 or len(comm2_dict) == 0:
            break

    print("\nCombat ended. Commanders, please wait while finalising results.")

    while q < 1000000:
        q += 1

    # Results declaration
    if len(comm1_dict) == 0 and len(comm2_dict) != 0:
        print("\nFinally, it's a Commander 2 Win")
    elif len(comm1_dict) != 0 and len(comm2_dict) == 0:
        print("\nFinally, it's a Commander 1 Win")
    else:
        print("\nFinally, it's a Tie")
except Exception as e:
    print("Exception occurred. Please restart the game.",e)