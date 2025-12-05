from apps import compint, infl


# help command
class help():
    def main():
        print("""Available commands:
    - compint: A compound interest calculator.
    - inflation: An inflation rate calculator.
    - help: Show this help message.
""")

# define commands dict so that we can call apps by name.
cmds = {
    "help": help,
    "compint": compint,
    "inflation": infl
}

# define main loop
def main():
    while True:
        cmd = input("Enter the app you would like to run. For help, type \"help\": ").strip().lower()
        if cmd in cmds:
            cmds[cmd].main()
        else:
            print("Unrecognized command. Type \"help\" for a list of available commands.")

# run main loop
if __name__ == "__main__":
    main()