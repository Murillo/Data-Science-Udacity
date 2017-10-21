import sys
import string
import logging

from util import mapper_logfile
logging.basicConfig(filename=mapper_logfile, format='%(message)s',
                    level=logging.INFO, filemode='w')

def mapper():
    
    #Also make sure to fill out the reducer code before clicking "Test Run" or "Submit".

    #Each line will be a comma-separated list of values. The
    #header row WILL be included. Tokenize each row using the 
    #commas, and emit (i.e. print) a key-value pair containing the 
    #district (not state) and Aadhaar generated, separated by a tab. 
    #Skip rows without the correct number of tokens and also skip 
    #the header row.

    #You can see a copy of the the input Aadhaar data
    #in the link below:
    #https://www.dropbox.com/s/vn8t4uulbsfmalo/aadhaar_data.csv

    #Since you are printing the output of your program, printing a debug 
    #statement will interfere with the operation of the grader. Instead, 
    #use the logging module, which we've configured to log to a file printed 
    #when you click "Test Run". For example:
    #logging.info("My debugging message")
    #
    #Note that, unlike print, logging.info will take only a single argument.
    #So logging.info("my message") will work, but logging.info("my","message") will not.
    
    dist = 0
    adge = 0
    for line in sys.stdin:
        data = line.split(',')
        if data[3] == "District":
            dist = data.index("District")
            adge = data.index("Aadhaar generated")
        else:
            output = data[dist] + '\t' + data[adge]
            print output

mapper()
