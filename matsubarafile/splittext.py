import sys
args = sys.argv

input_text = str(args[1])
tag_number = int(args[2]) -1

textsplit =[]
textsplit = input_text.split(" ")
print(textsplit[tag_number] , end ="")
