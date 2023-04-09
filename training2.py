number = {
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four"
}
output = ""
ask = input("phone: ")
for numbers in ask :
  print(number.get(numbers))
