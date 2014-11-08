import sys
import os

def process( filename, dir ):
   
   file = open( os.path.join(root, filename) ).readlines()
   
   outfile_name = "{0}/changed/{1}_alt.csv".format(dir, filename[:len(filename)-4])
   dir0 = os.path.dirname( outfile_name )
   if not os.path.exists( dir0 ):
      os.makedirs( dir0 )
   f = open( outfile_name, "w" )
   
   ok_write = False
   
   for line in file:
      if "PA1000 0001 Ch1 " in line and not ok_write:
         ok_write = True

      if ok_write:
         f.write( "{0}".format(line.replace("PA1000 0001 Ch1 ", ''))) 


   f.close()


if __name__ == '__main__':

   path = sys.argv[1]
   
   print path
   
   for root, dirs, filenames in os.walk(path):

      for fn in filenames:

         if fn.endswith(".csv") and 'pa' in fn:

            process(fn, root)


