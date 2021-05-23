#!/usr/local/bin/python3
import sys
import os



def determine_phone_lines(houseLocations):

    phoneTowerCount = 0;
    lastTowerLocation = 0;


    print("Tower Locations:")
    for line in houseLocations:
        temp = int(line.strip())
        
        
        if(phoneTowerCount == 0 or temp > lastTowerLocation + 4):
            phoneTowerCount += 1
            lastTowerLocation = temp + 4
            print(lastTowerLocation)

    print("Total Towers Needed: ")
    print(phoneTowerCount)




def read_file(fileName):
    
    houseLocations = open(fileName, "r")
#Safety checks to make sure that the file is valid


    determine_phone_lines(houseLocations)




def main():
    


    read_file("group1.txt")







if __name__ == "__main__":
    main()

