import json
import os
import time


class SaveFile:
    def __init__(self, data: dict):
        self.data = data

    def save(self):
        with open("saves/" + self.data["name"] + ".json", "w") as f:
            json.dump(self.data, f, indent=2)
        f.close()

    def load(self, name: str):
        with open("saves/" + name + ".json") as f:
            data = json.load(f)
        self.data = data
        f.close()

    def delete(self):
        os.remove("saves/" + self.data["name"] + ".json")
        del self


def delete_save_file(name: str):
    os.remove("saves/" + name + ".json")


def save_exists(name: str):
    return os.path.exists("saves/" + name + ".json")


def list_of_saves():
    return map(lambda x: x.split(".")[0], os.listdir("saves"))


if not os.path.exists("saves"):
    os.mkdir("saves")

if __name__ == "__main__":
    print("You picked wrong house, fool!")
    time.sleep(2)
