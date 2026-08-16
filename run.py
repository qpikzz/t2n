from t2n import *

# inf loop
def main(working):
    while working:  # ctrl + c to stop ts
        command = input()
        clearCommand = command.strip().split(" ")

        if clearCommand[0].lower() in ["exit", "quit"]:
            working = False

        elif clearCommand[0].lower() in ["help", "commands"]:
            with open("help.txt") as helpFile:
                print(helpFile.read())

        elif clearCommand[0].lower() == "ttn":
            if len(clearCommand) <= 1:
                print("Insufficient data. Use the help command.")
                continue

            alpName = clearCommand[1].lower()

            try:
                with open(f"alphabets/{alpName}.txt", encoding="utf-8") as f:
                    alp = f.readline()
                result = text_to_number(" ".join(clearCommand[2:]), alp)
                print(result)

            except FileNotFoundError:
                print(
                    f"the list of alphabets does not include \"{alpName}\"\ncheck the correctness of the command or the contents of the directory with alphabets.")

            except ValueError:
                print("the alphabet is not able to process this text.")

        elif clearCommand[0].lower() == "ntt":
            if len(clearCommand) <= 1:
                print("Insufficient data. Use the help command.")
                continue

            alpName = clearCommand[1].lower()

            try:
                with open(f"alphabets/{alpName}.txt", encoding="utf-8") as f:
                    alp = f.readline()
                result = number_to_text(int(clearCommand[2]), alp)
                print(result)

            except FileNotFoundError:
                print(
                    f"the list of alphabets does not include \"{alpName}\"\ncheck the correctness of the command or the contents of the directory with alphabets.")

            except ValueError:
                print("You are write not a number")

        else:
            try:
                print(eval(command))
            except Exception as e:
                print(e)

if __name__ == "__main__":
    print("Welcome to T2N\nWrite \"help\" to show a list of commands")
    try:
        main(1)
    except KeyboardInterrupt:
        ...
    print("Bye!")