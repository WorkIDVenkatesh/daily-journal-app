emoji_fun ={
    "love":"🤟",
    "happy":"😃",
    "code":"👩‍💻",
    "tea":"🍵",
    "music":"🎶",
    "food":"🍔"
}

message = input("Enter your message: ")

updated_message = []

for word in message.split():
    cleaned = word.lower().strip(".,!?")
    emoji = emoji_fun.get(cleaned, "")
    if emoji:
        updated_message.append(f"{word} {emoji}")
    else:
        updated_message.append(word)

updated_words = " ".join(updated_message)
print("\n enanched message \n")
print(updated_words)