"""
Sellthing.co
Styx
Andwiseb

version: 0.2
"""


import tkinter as tk
from tkinter import filedialog
import os
from os import system
import os.path
import time
system("title " + "Mail Domain Sorter - Sellthing - Styx")
from datetime import date
from datetime import datetime

root = tk.Tk()
root.withdraw()


logTextSellhting = """
                                                             
   _|_|_|  _|                                                
 _|        _|_|_|      _|_|_|  _|  _|_|    _|_|    _|_|_|    
 _|        _|    _|  _|    _|  _|_|      _|    _|  _|    _|  
 _|        _|    _|  _|    _|  _|        _|    _|  _|    _|  
   _|_|_|  _|    _|    _|_|_|  _|          _|_|    _|    _|  
                                                             
                                                                                                                      
www.sellthing.co | Styx
"""
print(logTextSellhting)

def getStarted():
    
    print('Please separate each word with a comma (,). Example: test, test1, test2')
    getWords = input("Enter the words you want to split :")
    replace = getWords.replace(', ', ',').replace(',', ',').replace(' ', '').replace('\s+ ', '').replace(' ,', '').replace(' \s+', '')
    splitWords = ""

    if(getWords == ""):
        print('Please enter words.')
        getStarted();
    else:
        if(',' in replace):
            splitWords = replace.split(',')
        else:
            splitWords = replace

    splitWord(splitWords)
    



def splitWord(word): 
    print("-------------------------------------------")
    print("Select the file")
    print("-------------------------------------------")
    
    """ When the file selection panel is opened, we synchronize the uploaded file to file_path. """
    file_path = filedialog.askopenfile(mode ='r', filetypes =[('Text Files', '*.txt')])

    """ If the file is not selected, we send it to the beginning."""
    if(not file_path):
        print("You haven't selected a file!")
        print("-------------------------------------------")
        getStarted()
    
    if(file_path == None):
        print("Restart the program.")
        exit()
    
    """ If there is no folder named result it will create """
    if(not os.path.isdir('result')):
        os.mkdir('result')

    """ We have created an empty array so that we will put the words read into it."""
    findList = []


    """
        If the user is scanning more than one word, we check it.
        This is due to the following for and if codes.
    """

    now = datetime.now()
    getTime = now.strftime("%H-%M-%S")

    if(isinstance(word, list)):
        print("Completing the process please wait.")
        system("title " + "Mail Domain Sorter - Process has started.")
        for words in word:
            i = 0
            control = False
            """ We have the process of reading each line of the selected file. """
            for line in open(file_path.name, 'r').readlines():
                """ CPM Left Count """

                """ If the words given by the user are in the file, we check."""
                if words in line:
                    control = True
                    """
                        If there is a word in the file that the user searched for, a file of that word is opened below. Example: test1.txt
                    """
                    i += 1
                    open('result/' + os.path.basename(str(words) + " - " + getTime + '.txt'), 'w+')
                    findList.append(line)
            if control == True:
                """
                    The reason for checking the "Control" variable is to prevent creating a new file from each line in the file.
                """
                open("result/" + str(words) + " - " + getTime + '.txt', "w").writelines(findList)

                """ After all searches for a word are completed, we reset the records found. """
                findList = []
            print("Generate Process is Starting.")
            time.sleep(0.5)
            print("---------------------------------------------------")
            print(str(len(open('result/' + words + " - " + getTime +  '.txt').read().splitlines())) + " " + str(words) + " records found.")
            print("---------------------------------------------------")
            time.sleep(0.5)
                
    else:
        """ If the user has entered a single word, the actions will be done here. """
        print("Completing the process please wait.")
        system("title " + "Mail Domain Sorter - Process has started.")
        control = False
        i = 0
        for line in open(file_path.name, 'r').readlines():
            if word in line:
                control = True
                i += 1
                open('result/' + os.path.basename(str(word) + " - " + getTime + '.txt'), 'w+')
                findList.append(line)
        if control == True:
            open("result/" + str(word) + " - " + getTime + '.txt', "w").writelines(findList)
        else:
            print("No line found about " + word)


        print("---------------------------------------------------")
        print(str(len(open('result/' + word + " - " + getTime +  '.txt').read().splitlines())) + " " + word + " records found.")
        print("---------------------------------------------------")
        
    time.sleep(0.5)
    print("The program shuts down...")
    time.sleep(0.4)
    print("Bye")
    time.sleep(3)
    

        

getStarted()