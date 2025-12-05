import apps.infl
import os

# define compounding frequency dict
freq = {
    "yr": "years",
    "semi": "semiannual periods",
    "qtr": "quarters",
    "mth": "months",
    "wk": "weeks",
    "dly": "days"
}

#clear screen command
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
#main function
def main():
    clear()
    print("Welcome to the FINANCIER™ COMPOUND INTEREST CALCULATOR. To return the main menu, type \"quittomain\". To quit the program, type \"quittocmd\"")
    input("Press ENTER/RETURN to continue.")
    clear()
    f = input("Input the frequency (F) of compounding (yr, semi, qtr, mth, wk, dly): ").strip().lower()
    if f in freq:
        n = freq[f]
    else:
        print("Unrecognized frequency. Defaulting to yearly compounding.")
        n = "years"
    P = float(input("Input the initial investment/principal amount (P): $"))
    r = float(input("Input the annual interesst rate (r) (as a percentage; i.e, 5): ")) / 100
    t = float(input("Input the total investment time (t) (as an integer): "))
    output = round((P * (1 + r)**t), 2)
    print(f"The total amount (A) after {round(t)} {n} is: ${output}")
    input("Press ENTER/RETURN to return to the main menu.")
    clear()
    return