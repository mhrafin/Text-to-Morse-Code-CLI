import pandas as pd

# Get the the data into a dictionary so that it can be called using keys which are the letters.
data = pd.read_csv("data.csv", index_col=0)

# Get the text from the user.
print("Welcome to Text to Morse code Converter!")
text = input("Insert a text (a-z,0-9): ").lower()
text_list = list(text)

print(f"Morse code for {text}: ", end="")
for letter in text_list:
    print(data["code"][letter], end="")
print()


