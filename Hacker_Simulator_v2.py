import savefile
import language


# lets type only your chosen variants in given list, or just normal input() if no arguments involved
def expect_input(lst=None, message=None):
    while True:
        inp = input("\n>>>")
        if not lst:
            return inp
        if inp in lst:
            return inp


def get_language_dict():
    languages_dict = language.dict_of_all_languages()
    possible_inputs = []
    for key in languages_dict.keys():
        possible_inputs += str(key)
        print(key, "->", languages_dict[key])
    choise = int(expect_input(possible_inputs))
    return language.extract_language_pack(choise)


def text(ind):
    if type(ind) == str:
        return TEXT[ind]
    else:
        return TEXT[str(ind)]


def manage_save_files():
    while True:
        print(text(0))
        print(text(1))

        current_save = savefile.SaveFile(dict())
        if expect_input(["1", "2"]) == "1":
            print(text(2))
            name = expect_input()

            if savefile.save_exists(name):
                print(text(3))
                if expect_input([text("yes"), text("no")]) == text("no"):
                    continue

            current_save.data["name"] = name
            current_save.data["skill"] = 1
        else:
            print(text(4))
            saves = dict()
            for i, save_name in enumerate(savefile.list_of_saves(), 1):
                saves[i] = save_name
                print(save_name, f"[{i}]")

            inp = expect_input([str(i) for i in range(1, len(saves) + 1)])

            current_save.load(saves[int(inp)])
        break
    current_save.save()


if __name__ == "__main__":
    TEXT = get_language_dict()
    manage_save_files()
