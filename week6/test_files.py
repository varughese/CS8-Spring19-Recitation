new_file = open("test.txt", mode="w+", encoding="utf-8")
new_file.write("Hello")
new_file.close()

file = open("test.txt", mode="r", encoding="utf-8")
string_in_file = file.read()
print(string_in_file)