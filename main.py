#!/usr/local/bin/python3

import tkinter as tk
from tkinter import messagebox
import sys
import os
from os import path

window = tk.Tk()
window.title("Base Station Planner")
window.geometry("300x350")

label = tk.Label(text = "File Name: ")
entry = tk.Entry()
output = tk.Label()


def determine_phone_lines(houses):

    baseStationCount = 0
    lastStationLocation = 0
    outputStr = "Base Station Locations: \n"
    for i in houses:
        if(baseStationCount == 0 or i > lastStationLocation + 4):
            baseStationCount += 1
            lastStationLocation = i + 4
            outputStr += str(lastStationLocation)
            outputStr += " miles\n"

    outputStr += "Total Base Stations Needed: "
    outputStr += str(baseStationCount)   
    output.config(text = outputStr)



def read_file():

    if entry.get() == '':
        tk.messagebox.showerror(title = "Error", message = "Please enter a file name")
    else:
        if path.exists(entry.get()) == True:
            houseLocations = open(entry.get(), "r")
            houses = []
            for line in houseLocations:
                houses.append(float(line.strip()))
                  
            houses = sorted(houses, key = float)
            houseLocations.close()
            determine_phone_lines(houses)
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
