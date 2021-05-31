#!/usr/local/bin/python3

import tkinter as tk
from tkinter import messagebox
import sys
import os
from os import path


window = tk.Tk()
window.title("Powerline Planner")
window.geometry("300x350")

label = tk.Label(text = "File Name: ")
entry = tk.Entry()
output = tk.Label()


def determine_phone_lines(houseLocations):

   

    outputStr = "Base Station Locations: \n"



    phoneTowerCount = 0
    lastTowerLocation = 0


    print("Base Station Locations:")




    for line in houseLocations:
        temp = float(line.strip())
        
        
        if(phoneTowerCount == 0 or temp > lastTowerLocation + 4):
            phoneTowerCount += 1
            lastTowerLocation = temp + 4
            outputStr += str(lastTowerLocation)
            outputStr += " miles\n"



    outputStr += "Total Base Stations Needed: "
    outputStr += str(phoneTowerCount)

   
    output.config(text = outputStr)

    houseLocations.close()



def read_file():

    if entry.get() == '':
        tk.messagebox.showerror(title = "Error", message = "Please enter a file name")
    else:
        if path.exists(entry.get()) == True:
            houseLocations = open(entry.get(), "r")
            determine_phone_lines(houseLocations)
        else:
            tk.messagebox.showerror(title = "Error", message = "File not Found")






def main():
    

    button = tk.Button(text = "Enter ", command = read_file).grid(row = 1, column = 0)
    label.grid(row = 0, column = 0)
    entry.grid(row = 0, column = 1)
    output.grid(row = 2, column = 0)

    window.mainloop()







if __name__ == "__main__":
    main()
