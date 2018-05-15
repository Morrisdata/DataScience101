
###############################################################################
'''
Python for Data I 
Reading files

MATTHEW MORRIS
matthewmorris.da@gmail.com
advanced analytics analyst and instructor
'''
###############################################################################

# Enter one line of comments
''' 
Enter
Multiple 
Lines 
Of
Comments
'''
###############################################################################
##                       NICE HEADERS                                        ##
###############################################################################

print 'we wont be learning Hello World' # inline commments should be avoided

##
#Excercise
##



# OK lets get started with 
###############################################################################
##                       WORKING WITH FILES                                  ##
'''
 Covered in this Unit
- import
- getcwd()
- chdir()
- listdir()
- shutil(source,destination)
- open readlines
- close()
'''
###############################################################################

'''
First step in working with files is being able to navigate to your files or 
save your files using python programing rather than your file explorer.
lets first start by reading some files in. You downloaded data from GitHUB. 
Hopefully you have had a chance to unzip the file and 
Let's start looking at this in python 
'''
# Set your OS path where your files are stored

# getcwd() What is your Current Working directory 
import os
os.getcwd()

# chdir() Change your default working directory - you dont want to do this often
import os
from pathlib import Path

path = Path('//Users//Matthew//Desktop//SANDBOX/TEST/DATA')
os.chdir(path)

## EXERCISE
# Get Current working directory
##




# listdir() List all of the files in your directory

import os
files = os.listdir()
files
os.getcwd()

# shutil(src,dst) Move files
'''
1. Create a two folders on your desktop 1 called Hotel and 1 called Conference.
    feel free to do this manually or via gitbash 
2. Create a file in your source folder called passenger.txt
3. Change your working directory to your desktop
4. Use shutil to move your passenger file back and forth from your Hotel to Conference
5. Check your folders to validate the file has moved, then try moving it back
'''
import shutil
shutil.move('C://Users//Matthew//Desktop//Hotel//passenger.txt', /
            'C://Users//Matthew//Desktop//Conference//passenger.txt')



'''
We will be using a lot of variables in our code. Loading your file path into a
variable will make it more flexible
'''

import shutil
hotel = 'C://Users//Matthew//Desktop//Hotel//passenger.txt'
conference = 'C://Users//Matthew//Desktop//Conference//passenger.txt'
shutil.move(conference,hotel)

## EXERCISE
# Use shutil to 
# Move sales.csv, products.csv, stores.csv, counties.csv into a new folder
# Iowa Liquor Sales
##



# READING AND WRITING

# open readlines 
counties = open("counties.csv") # you may need to work with your path
counties.readlines()


# notice the \n that is a carraige return or enter key. 

## EXERCISE
# open and read each of the files in the iowa liquor sales database
##





# time to create files, read files and write to files

# Open a file to write to 'W' or create one '+'
a = open("new_file.csv","w+")

# open your folder and see if the file was created

# Write a line to the document
a.write("First line in my doc.")
# Close file
a.close()

#Open file into variable
b = open("new_file.csv","r")
# use readlines to readlines into a variable
c = b.readlines()
b.close()
# output results to the screen
(c)


# Write several lines to a file and read them
		
t = open("multiline.csv", 'w+')			

# Use Raw_inputs to create 3 lines of in your file
line1 = "line 1,Red"
line2 = "line 2,Blue"
line3 = "line 3,Green, 4.52"

t.write(line1)
t.write("\n")   # \n is a carriage return that we are writing to file
t.write(line2)
t.write("\n")
t.write(line3)
t.write("\n")
t.close()

a = open("multiline.csv","r")
b = a.readlines()
a.close()
b



# Find your file and review it

'''
line1 = "line 1"
line2 = "line 2"
line3 = "line 3"
in the above code that you just ran try putting commas and more information
Then review your file again to see how it behaves
Example

line1 = "line 1,Red"
line2 = "line 2,Blue"
line3 = "line 3,Green, 4.52"

'''

## EXERCISE
# Create a file called names with names of friends family actors or fictional characters
# column for First Name, Last Name, age, Notes
##



# 'a+' Next append a line to the end of the file
# Open the file for appending text to the end
t= open("multiline.csv","a+")
t.write("append_test, 4")
t.close()
t

## EXERCISE
# Reopen your name file and add a new name to the file 
##




''' PROJECT EXERCISE 
Create a file that lists all the skills you have learned so far
rate yourself for each skill in a seperate column next to the skill
0 = Don't know
1 = Aquiring knowledge
2 = Can apply with 80% help from Google
3 = Can apply with 20% help from Google
4 = Can teach <20% help from Google
5 = Can design, review, optimize
What is your average score?
What areas are you doing great in, what areas do you need to study?
This Project will grow and be designed and redesigned several different ways
as you progress and revist.'''

###############################################################################
'''
Want to learn more?
Check out:
SQL Bootcamp
Python for Data I, II, III
https://generalassemb.ly/
'''
###############################################################################

