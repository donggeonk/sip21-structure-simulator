
#!/usr/bin/python3
import argparse
import sys
import os
import re
import csv

# global variables
a_list =  []
p0_list = []
p1_list = []
p2_list = []

rpl_idx = []

def gen_str (size, fout):
  b_list = []
  for i in range (size):
    b_list.append (a_list[i])

  for ptr in rpl_idx:
    b_list[ptr] = "N"

  for i in range (size):
    pline = b_list[i]+" "+p0_list[i]+" "+p1_list[i]+" "+p2_list[i];
    print (pline, file=fout)

def replace_one (size, fout):
  case = 0;
  rpl_idx.append(-1)
  for i in range (size):
    if (a_list[i] == "C") :
      case += 1
      rpl_idx[0] = i
      print (("# replace one: case="+str(case) + " pos="+str(rpl_idx)), file=fout)
      gen_str (size, fout)

def replace_two (size, fout):
  rpl_idx.append(-1)
  rpl_idx.append(-1)
  case = 0;

  for i in range (size-1):
    if (a_list[i] == "C") :
      rpl_idx[0] = i
      for j in range(i+1, size):
        if (a_list[j] == "C"):
          case += 1
          rpl_idx[1] = j
          print (("# replace two: case="+str(case) + " pos="+str(rpl_idx)), file=fout)
          gen_str (size, fout)


def main():

   parser = argparse.ArgumentParser()
   parser.add_argument("-i", "--input",   help = "input  filename")
   parser.add_argument("-o", "--output",  help = "output filename")
   parser.add_argument("-n", "--number",  help = "replace number")

   args = parser.parse_args()

   print('inputfile:', args.input)
   print('outputfile:', args.output)
   print('number:', args.number)

   # read input
   fin = open(args.input, 'r')
   size = 0;
   for line in fin:
     # print line
     m = re.match(r'^([A-Z])\s+(\S+)\s+(\S+)\s+(\S+)', line)
     if m:
       a_list.append(m.group(1))
       p0_list.append(m.group(2))
       p1_list.append(m.group(3))
       p2_list.append(m.group(4))
       size += 1
   fin.close()

   print ("size="+str(size))

   fout = open(args.output,'w')

   num = int(args.number)

   if (num == 1):
     replace_one(size, fout)
   elif (num == 2):
     replace_two(size, fout)

   fout.close()


if __name__ == '__main__':
    main ()