print("Welcome to Manga Reader of Temperature !")
print("Answer a few questions to get started you?.")

genre = input("What genre are you? (action, romance, horror): ").lower()

duration = input("How long should a manga volume be? (long, medium, short): ").lower()

time = input("How many decade? (2000s, 2010s): ").lower()

if genre == "action":
    if duration == "long": 
        if time == "2000s" or time == "2000": 
            print("\nThe available mangas are: ")

elif time == "2010s" or time == "2010": 
    print("\nThe available mangas are: ")

if duration == "medium":
    if time == "2000s" or time == "2000": 
        print("\nThe available mangas are: ")

elif time == "2010s" or time == "2010": 
    print("\nThe available mangas are: ")

if duration == "short":
    if time == "2000s" or time == "2000": 
        print("\nThe available mangas are: ")

elif time == "2010s" or time == "2010": 
    print("\nThe available mangas are: ")

if genre == "romance":
    if duration == "long": 
        if time == "2000s" or time == "2000": 
            print("\nThe available mangas are: ")

elif time == "2010s" or time == "2010": 
    print("\nThe available mangas are: ")

if duration == "medium":
    if time == "2000s" or time == "2000":
        print("\nThe available mangas are: ")

elif time == "2010s" or time == "2010": 
    print("\nThe available mangas are: ")

if duration == "short":
    if time == "2000s" or time == "2000": 
        print("\nThe available mangas are: ")

elif time == "2010s" or time == "2010": 
    print("\nThe available mangas are: ")

if genre == "horror":
    if duration == "long":
        if time == "2000s" or time == "2000": 
            print("\nThe available mangas are: ")

elif time == "2010s" or time == "2010": 
    print("\nThe available mangas are: ")

else:
    print("\nSorry, no mangas found for your choices.")
