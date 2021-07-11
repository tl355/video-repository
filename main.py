import os.path
import json
import webbrowser


# Helper Functions
def represents_int(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def add_link(link, title):
    with open(os.getcwd() + "\\video.json", "r") as read_file:
        to_add = json.load(read_file)
    # Check for Duplicate Title:
    for i in range(len(to_add)):
        if title == to_add[i][0]:
            print("There already exists a link with this title. Addition Failed.")
            return
        if link == to_add[i][1]:
            print("This link already exists in the database under \"" + to_add[i][0] + "\".")
            return

    to_add.append([title, link])
    with open(os.getcwd() + "\\video.json", "w") as write_file:
        json.dump(to_add, write_file)
    print("Addition successful.")
    return


def display_videos():
    with open(os.getcwd() + "\\video.json", "r") as read_file:
        videos = json.load(read_file)
    if not videos:
        print("No videos stored.")
    else:
        for i in range(len(videos)):
            print(str(i+1).ljust(3) + " - " + videos[i][0])
    return


def get_size():
    with open(os.getcwd() + "\\video.json", "r") as read_file:
        videos = json.load(read_file)
    return len(videos)


def remove_video(index):
    with open(os.getcwd() + "\\video.json", "r") as read_file:
        videos = json.load(read_file)
    del videos[index]
    with open(os.getcwd() + "\\video.json", "w") as write_file:
        json.dump(videos, write_file)
    return


def open_link(index):
    with open(os.getcwd() + "\\video.json", "r") as read_file:
        videos = json.load(read_file)
    print("Opening video \"" + videos[index][0] + "\"...")
    webbrowser.open(videos[index][1])


# Main Function
if not(os.path.isfile(os.getcwd() + "\\video.json")):
    file = open(os.getcwd() + "\\video.json", "w")
    json.dump([], file)
    file.close()

print("Welcome to the YouTube Video Repository!")
while True:
    print("1 - Open a Video")
    print("2 - Add a Video")
    print("3 - Remove a Video")
    print("4 - Display Currently Stored Videos")
    print("5 - Exit")

    choice = input("Enter your selection here: ")
    while (choice != "1") & (choice != "2") & (choice != "3") & (choice != "4") & (choice != "5"):
        choice = input("Enter your selection here: ")

    if choice == "1":
        display_videos()
        while get_size() != 0:
            to_open = input("Which video would you like to open? (or type 0 to cancel): ")
            if not represents_int(to_open):
                print("Invalid input, please try again.")
            elif int(to_open) == 0:
                break
            elif (int(to_open) < 1) | (int(to_open) > get_size()):
                print("Invalid input, please try again.")
            else:
                open_link(int(to_open) - 1)
                break

    if choice == "2":
        while True:
            link_to_add = input("Enter the YouTube link here (or type 0 to cancel): ")
            if link_to_add == "0":
                break
            elif link_to_add.startswith("https://www.youtube.com/watch?v="):
                identifier = input("Enter an identifier here: ")
                add_link(link_to_add, identifier)
                break
            else:
                print("Invalid YouTube Link, please try again.")

    if choice == "3":
        display_videos()
        while get_size() != 0:
            to_remove = input("Which video would you like to remove? (type 0 to cancel, or -1 to clear all): ")
            if not(represents_int(to_remove)):
                print("Invalid input, please try again.")
            elif int(to_remove) == 0:
                break
            elif int(to_remove) == -1:
                with open(os.getcwd() + "\\video.json", "w") as to_delete:
                    json.dump([], to_delete)
                print("All videos removed.")
                break
            elif (int(to_remove) > get_size()) | (int(to_remove) < 1):
                print("Invalid value, please try again.")

            else:
                remove_video(int(to_remove) - 1)
                print("Video removed.")
                display_videos()

    if choice == "4":
        display_videos()

    if choice == "5":
        exit()

    print()
