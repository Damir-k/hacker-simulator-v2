import SF


def expect_input(lst=None):
    while True:
        inp = input("\n>>>")
        if not lst:
            return inp
        elif inp in lst:
            return inp


#  eng, rus
# TEXT = {
#     0: ["Hello world", "Привет, мир"],
#     1: ["Hope you doin' great", "Все у тебя хорошо?"]
# }
# language = expect_input("eng", "rus")
# index = 0 + int(language == "rus")
# print(TEXT[0][index])
# print(TEXT[1][index])


def manage_save_files():
    #  starting animation
    while True:
        print("Create new save [1]")
        print("Load existing save [2]")

        current_save = SF.SaveFile(dict())
        if expect_input(["1", "2"]) == "1":
            print("Choose your save name")
            name = expect_input()

            if SF.save_exists(name):
                print("This save already exist. Overwrite save? [y/n]")
                if expect_input(["y", "n"]) == "n":
                    continue

            current_save.data["name"] = name
            current_save.data["skill"] = 1
        else:
            print("Choose your save")
            saves = dict()
            for i, save_name in enumerate(SF.list_of_saves(), 1):
                saves[i] = save_name
                print(save_name, f"[{i}]")

            inp = expect_input([str(i) for i in range(1, len(saves) + 1)])

            current_save.load(saves[int(inp)])
        break
    current_save.save()


if __name__ == "__main__":
    manage_save_files()
