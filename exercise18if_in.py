#movies_watched = {"The Matrix", "Green Book", "Her"}
#user_movie = input("enter something you've watched recently: ")

#if user_movie in movies_watched:
 #   print(f"I've watched {user_movie} too!")
#else:
 # print("I have not seen that.")

number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input in ("y","Y"):
    user_number = int(input("Guess our number: "))
if user_number ==number:
    print("you guessed correctly!")
elif number - user_number in (1,-1):
    print("You were off by one.")
else:
    print("sorry, it's wrong!")
  


