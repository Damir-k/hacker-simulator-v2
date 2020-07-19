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


def manage_languages():
    languages_set = language.languages_set()

    keys = []
    for key in languages_set.keys():
        keys += str(key)
        print(key, "->", languages_set[key])
    key = int(expect_input(keys))

    return language.load_language_pack(key)


def manage_saves(text):
    while True:  # get save loop
        print(text["0"])  # load/create
        current_save = savefile.SaveFile(dict())

        if expect_input(["1", "2"]) == "1":
            print(text["1"])  # new save name
            save_name = expect_input()

            if savefile.save_exists(save_name):
                print(text["2"])  # save already exist. recreate?
                if expect_input([text["yes"], text["no"]]) == text["no"]:
                    continue

            current_save.data["name"] = save_name  # new save parameters
            current_save.data["skill"] = 1
        else:
            print(text[3])  # load old save from the list below

            saves = dict()
            for i, save_name in enumerate(savefile.list_of_saves(), 1):  # printing all the saves
                saves[i] = save_name
                print(save_name, f"[{i}]")
            inp = expect_input([str(i) for i in range(1, len(saves) + 1)])

            current_save.load(saves[int(inp)])
        break
    current_save.save()  # save to file immediately
    return current_save


def main():
    language_pack = manage_languages()
    save = manage_saves(language_pack)


if __name__ == "__main__":
    main()
