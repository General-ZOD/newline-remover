"""
Read the README.md file in the folder  
"""

import os, sys, time

def main(_file):
    path = os.path.dirname(_file) + os.path.sep
    temp_file = path + str(time.time())
    if (not os.path.isfile(_file)): exit("File submitted does not exist. Please, run the application again, supplying the proper file's absolute path")
    try:
        with open(_file, "r") as from_file, open(temp_file, "a") as to_file:
            while True:
                each_line = from_file.readline()
                if not each_line: break
                each_line = each_line.rstrip("\r\n")
                if each_line: to_file.write(each_line + "\r\n")
            from_file.close()    
            os.rename(temp_file, _file)
    except Exception, e:
        print "The following error has occurred\n", e

if __name__ == "__main__":
    if len(sys.argv) < 2: exit("File's absolute path must be specified")
    _file = sys.argv[1]
    main(_file)