message = input(">")
message.split(' ')

emojis = {
    ":)" : "😂",
    ":(" : "😞"
}
output= ""
for word in message.split(' '):
   output += emojis.get(word, word) + " "
print(output)