
def Menu():
    print("\nMenu: \n1: Start New Seed Stock \n2: Add Seed Stock \n3: Get Seed Stock")
    selection = input("\nPlease select an option: ")

    if(selection == '1'):
        invID = input("Enter the new ID for the new Seed Stock: ")
        newPN = input("Please enter the Part Number: ")
        newCount = input("What is the count for this part? ")
        newDesc = input("Please enter the part description: ")

        inventory = {}
        seedStock = {}
        inventory["Part Number"] = newPN
        inventory["Count"] = newCount
        inventory["Description"] = newDesc
        seedStock[invID] = inventory
        with open('test.txt', 'w') as fp:
            fp.write(str(seedStock))
            
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

Menu()
