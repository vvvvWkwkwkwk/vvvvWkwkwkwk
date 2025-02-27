test = input("Is it raining? y/n ")
if test in ["y","Y","Yes","yes"]:
    print("Oh dear, no football today!")
elif test in ["na","n","N","nein","no","No","No lmao","no lmao","Na","Nein"]:
    print("Let's play football!")
else:
    print("Thanks for your input, however I have no idea what you are saying little buddy.")
