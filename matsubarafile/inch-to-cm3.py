import sys
args = sys.argv

per_inch = 2.54
inch = int(args[1])
cm = inch * inch
desc = "{0} = {1}センチ".format(inch,cm)
print(desc)