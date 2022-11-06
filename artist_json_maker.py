import json
import os

artist = input("What artists lyrics are we storing today? ")
file_name = artist + ".json"


def json_check(artist_name):
    return os.path.exists(artist_name)


if json_check(f'{file_name}'):
    pass

else:
    file = open(file_name, "w+")
    file.write("[]")
    file.close()
    # with open('data.json', 'w') as outfile:
    #     json.dump(data, outfile)


def choices():
    print(f" *** {artist.capitalize()} *** J S O N *** Maker")
    print("Data Management system")
    print("(1) View data")
    print("(2) Add data")
    print("(3) Edit data")
    print("(4) Delete data")
    print("(5) Exit")


def view_data():
    with open(file_name, "r") as f:
        temp = json.load(f)
        i = 0
    for entry in temp:
        lyric = entry["lyric"]
        song = entry["song"]
        album = entry["album"]
        print(f"Index Number: {i}")
        print(f"Lyric: {lyric}")
        print(f"Song: {song}")
        print(f"Album: {album}")
        print("\n\n")
        i = i + 1


def delete_data():
    view_data()
    new_data = []
    with open(file_name, "r") as f:
        temp = json.load(f)
        data_length = len(temp) - 1
    print("which index number would you like to delete?: ")
    delete_option = input(f"Select a number 0 - {data_length} ")
    i = 0
    for entry in temp:
        if i == int(delete_option):
            pass
            i = i + 1
        else:
            new_data.append(entry)
            i = i + 1
    with open(file_name, "w") as f:
        json.dump(new_data, f, indent=4)


def edit_data():
    view_data()
    new_data = []
    with open(file_name, "r") as f:
        temp = json.load(f)
        data_length = len(temp) - 1
    print("which index number would you like to edit?: ")
    edit_option = input(f"Select a number 0 - {data_length} ")
    i = 0
    for entry in temp:
        if i == int(edit_option):
            lyric = entry["lyric"]
            song = entry["song"]
            album = entry["album"]
            print(f"Current lyric: {lyric}")
            lyric = input("What should the new lyric be?: ")
            print(f"Current song title: {song}")
            song = input("What should the song title be?: ")
            print(f"Current album title: {album}")
            album = input("What should the album title be?: ")
            new_data.append({"lyric": lyric, "song": song, "album": album})
            i = i + 1
        else:
            new_data.append(entry)
            i = i + 1
    with open(file_name, "w") as f:
        json.dump(new_data, f, indent=4)


def add_data():
    item_data = {}
    with open(file_name, "r") as f:
        temp = json.load(f)
    item_data["lyric"] = input("Whats the song Lyric?: ")
    item_data["song"] = input("Whats the song name?: ")
    item_data["album"] = input("What album is it in?: ")
    temp.append(item_data)
    with open(file_name, "w") as f:
        json.dump(temp, f, indent=4)


while True:

    choices()
    choice = input("\nEnter Number: ")
    if choice == "1":
        view_data()
    elif choice == "2":
        add_data()
    elif choice == "3":
        edit_data()
    elif choice == "4":
        delete_data()
    elif choice == "5":
        break
    else:
        print("You did not enter a number, please try again.")
