def intro():
    print("You wake up in a dark forest. You can go left or right.")
    choice = input("Which direction do you choose? (left/right): ").strip().lower()
    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("You stand still, unsure what to do. The forest swallows you.")

def left_path():
    print("You walk left and find a mysterious glowing sword stuck in a stone.")
    print("You pull the sword out quickly, with ease, surprised at how light it felt.")
    print("Suddenly, you're confronted by a restless dragon. It charges you, but you quickly slay it.")

def right_path():
    print("You walk right and encounter a talking squirrel who challenges you to a duel.")

if __name__ == "__main__":
    intro()
