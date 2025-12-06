import apps
import os
import apps.inflation

# define compounding frequency dict
freq = {
    "yr": 1,
    "semi": 2,
    "qtr": 4,
    "mth": 12,
    "wk": 52,
    "dly": 365
}

# input check function
def inpCheck(userinput):
    if userinput == "quittomain":
        return "__QUIT_MAIN__"
    elif userinput == "quittocmd":
        clear()
        exit()
    elif userinput == "restart":
        return "__RESTART__"
    return

# clear screen command
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# main function
def main():
    # initialize app
    clear()
    print("Welcome to the FINANCIER™ COMPOUND INTEREST CALCULATOR. To return the main menu, type \"quittomain\". To quit the program, type \"quittocmd\"")
    input("Press ENTER/RETURN to continue.")
    clear()
    # get user inputs
    f = input("Input the frequency (F) of compounding (yr, semi, qtr, mth, wk, dly): ").lower()
    check = inpCheck(f)
    if check == "__QUIT_MAIN__":
        clear()
        return
    elif check == "__RESTART__":
        clear()
        main()
        return
    if f in freq:
        fn = freq[f]
    else:
        print("Unrecognized frequency. Defaulting to yearly compounding.")
        fn = 1
    P = input("Input the initial investment/principal amount (P): $")
    check = inpCheck(P)
    if check == "__QUIT_MAIN__":
        clear()
        return
    elif check == "__RESTART__":
        clear()
        main()
        return
    try:
        P = float(P)
    except:
        print("Invalid principal amount. Defaulting to $1000.")
        P = 1000.0
    r = input("Input the interest rate (r) (as a percentage, not a decimal; i.e, 2.5): ")
    check = inpCheck(r)
    if check == "__QUIT_MAIN__":
        clear()
        return
    elif check == "__RESTART__":
        clear()
        main()
        return
    try:
        r = float(r) / 100
    except:
        print("Invalid interest rate. Defaulting to 2.5%.")
        r = 0.05
    t = input("Input the total investment time (t) (e.g., 10) (in years): ")
    check = inpCheck(t)
    if check == "__QUIT_MAIN__":
        clear()
        return
    elif check == "__RESTART__":
        clear()
        main()
        return
    try:
        t = float(t)
    except:
        print("Invalid time period. Defaulting to 10 years.")
        t = 10.0
    # adjust for inflation
    infladj = input("Will you be adjusting for inflation? (y/n): ").strip().lower()
    check = inpCheck(infladj)
    if check == "__QUIT_MAIN__":
        clear()
        return
    elif check == "__RESTART__":
        clear()
        main()
        return
    if infladj == "y":
        inflExpected = input("Will you be using [e]xpected or [h]istorical inflation rates? (e/h): ").strip().lower()
        check = inpCheck(inflExpected)
        if check == "__QUIT_MAIN__":
            clear()
            return
        elif check == "__RESTART__":
            clear()
            main()
            return
        try:
            inflT = float(input("Input the start year for inflation adjustment (i.e, 2004): "))
        except:
            print("Invalid year. Defaulting to 2004.")
            inflT = 2004.0
        check = inpCheck(inflT)
        if check == "__QUIT_MAIN__":
            clear()
            return
        elif check == "__RESTART__":
            clear()
            main()
            return
        if inflExpected == "e":
            inflRate = input("Input the expected average annual inflation rate (as a percentage, not a decimal; i.e, 3): ")
            check = inpCheck(inflRate)
            if check == "__QUIT_MAIN__":
                clear()
                return
            elif check == "__RESTART__":
                clear()
                main()
                return
            try:
                inflRate = float(inflRate) / 100
            except:
                print("Invalid inflation rate. Defaulting to 3%.")
                inflRate = 0.03
    output = round((P * (1 + r / fn) ** (fn * t)), 2)
    print(f"The total amount (A) after {round(t)} year{"s" if t != 1 else ""} is: ${output}")
    print(f"The total interest earned is: ${round((output - P), 2)}\n")
    check = inpCheck("Press ENTER/RETURN to return to the main menu.")
    if check == "__QUIT_MAIN__":
        clear()
        return
    elif check == "__RESTART__":
        clear()
        main()
        return
    clear()
    return