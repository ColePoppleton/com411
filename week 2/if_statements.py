
genres = ["adventure", "fantasy", "non-fiction", "sci-fi", "mystery"]

book = input("What type of book is this? \n")
if book in genres:
    print(f"I like {book} books")
    print("finished reading")
else:
    print("sorry not a valid genre")
