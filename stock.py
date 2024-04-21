import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

def AddSeed(invID, newPN, newCount, newDesc):
    inventory = {}
    seedStock = {}
    inventory["Part Number"] = newPN
    inventory["Count"] = newCount
    inventory["Description"] = newDesc
    seedStock[invID] = inventory
    with open('test.txt', 'w') as fp:
        fp.write(str(seedStock))

def Menu():
    print("\nMenu: \n1: Start New Seed Stock \n2: Add Seed Stock \n3: Get Seed Stock")
    selection = input("\nPlease select an option: ")

    if(selection == '1'):
        invID = input("Enter the new ID for the new Seed Stock: ")
        newPN = input("Please enter the Part Number: ")
        newCount = input("What is the count for this part? ")
        newDesc = input("Please enter the part description: ")

        AddSeed(invID, newPN, newCount, newDesc)

            
    elif(selection == '2'):

        invID = input("Enter the new ID for the new Seed Stock: ")
        newPN = input("Please enter the Part Number: ")
        newCount = input("What is the count for this part? ")
        newDesc = input("Please enter the part description: ")

        file = open('test.txt', 'rb')
        seed = file.read()
        seedStock = eval(seed)
        inventory = {}
        newSeedStock = {}
        inventory["Part Number"] = newPN
        inventory["Count"] = newCount
        inventory["Description"] = newDesc
        newSeedStock[invID] = inventory
        seedStock.update(newSeedStock)
        with open('test.txt', 'w') as fp:
            fp.write(str(seedStock))        
            
            
        Menu()
    
    elif(selection == '3'):
        with open('test.txt', 'rb') as handle:
            seed = handle.read()
            seedStock = eval(seed)
            print(seedStock)

            
            
        Menu()
    else:
        print("\nThank you for using this program!")

#Menu()

def make_window():
    #Creates the main window
    root = tk.Tk()
    #Sets the window size
    root.geometry("400x300")

    def clearWindow(): #clears the whole window of stuff
        for widget in root.winfo_children():
            widget.destroy()
    
    def mainMenu():
        clearWindow()
        #This is for the main menu
        title_label = tk.Label(root, text="Welcome to the stock program!\nWhat would you like to do today?", font=("Arial", 10))
        #The options for each
        B1 = Button(root, text ="Start New Seed Stock", command = newSeedStockMenu)
        B2 = Button(root, text ="Add Seed Stock", command = addSeedStockMenu)
        B3 = Button(root, text ="Get Seed Stock", command = getSeedStockMenu)

        #puts all of the elements on the window in order
        title_label.pack(pady=10)
        B1.pack(pady=10)
        B2.pack(pady=10)
        B3.pack(pady=10)
    
    def newSeedStockMenu():
        clearWindow() #clears the window to add more stuff

        title_label = tk.Label(root, text="Start New Seed Stock", font=("Arial", 10))
        
        
        #the comments are references to the original code
        #invID = input("Enter the new ID for the new Seed Stock: ")
        invID = tk.Label(root, text="ID: ", font=("Arial", 10))
        e1 = Entry(root)
        
        #newPN = input("Please enter the Part Number: ")
        newPN = tk.Label(root, text="Part Number: ", font=("Arial", 10))
        e2 = Entry(root)
        
        #newCount = input("What is the count for this part? ")
        newCount = tk.Label(root, text="Count: ", font=("Arial", 10))
        e3 = Entry(root)
        
        #newDesc = input("Please enter the part description: ")
        newDesc = tk.Label(root, text="Description: ", font=("Arial", 10))
        e4 = Entry(root)

        cur_y = 0
        x_pos = [150, 250]
        #places stuff down
        title_label.place(anchor=N, x=200, y=cur_y)
        cur_y += 35
        
        invID.place(anchor=N, x=x_pos[0], y=cur_y)
        e1.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newPN.place(anchor=N, x=x_pos[0], y=cur_y)
        e2.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newCount.place(anchor=N, x=x_pos[0], y=cur_y)
        e3.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35

        newDesc.place(anchor=N, x=x_pos[0], y=cur_y)
        e4.place(anchor=N, x=x_pos[1], y=cur_y)
        cur_y += 35
        
        #buttons for adding and canceling
        add_button = Button(root, text ="Add New Seed Stock", command = AddSeed(e1.get(), e2.get(), e3.get(), e4.get()))
        back_button = Button(root, text ="Back to menu", command = mainMenu)

        add_button.place(anchor=N, x=200, y=cur_y)
        cur_y += 35
        back_button.place(anchor=N, x=200, y=cur_y)
    
    def addSeedStockMenu():
        clearWindow() #clears the window to add more stuff
        
        title_label = tk.Label(root, text="Test", font=("Arial", 10))
        back_button = Button(root, text ="Back to menu", command = mainMenu)
        
        #adds more stuff
        title_label.pack(pady=10)
        back_button.pack(pady=10)
    
    def getSeedStockMenu():
        clearWindow() #clears the window to add more stuff
        
        title_label = tk.Label(root, text="Test", font=("Arial", 10))
        back_button = Button(root, text ="Back to menu", command = mainMenu)
        
        #adds more stuff
        title_label.pack(pady=10)
        back_button.pack(pady=10)
    


    mainMenu()

    #Shows the window
    root.mainloop()

make_window()