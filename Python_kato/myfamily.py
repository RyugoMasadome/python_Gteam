import sys
args = sys.argv

import introfamily

my_family = introfamily.IntroFam(args[1], args[2], args[3])
my_family.intropre()
my_family.cat_out()
