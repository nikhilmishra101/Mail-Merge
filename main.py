with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    starting_letter = letter.read()
    for name in names_list:
        stripped_names = name.strip()
        ready_letter = starting_letter.replace("name", f"{stripped_names}")
        with open(f"./Output/ReadyToSend/letter_for_{stripped_names}.txt", mode="w") as completed_letter:
            completed_letter.write(ready_letter)
















