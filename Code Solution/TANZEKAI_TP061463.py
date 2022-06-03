## TAN ZE KAI
## TP 061463

##########################################################################################################################

#### INSERT Parts that occured initially in three warehouses

# Function of writing into file

## Warehouse = [[1,2,3,4]]
## Section = [1,2,3,4]
## item = 1,2,3,4

def writeFile(fileName, warehouse, section):
    file = open(fileName,'w')
    for section in warehouse:   
        for item in section:
            file.write(item)
            file.write('\t')
        file.write('\n')
    file.close()
    return writeFile

def firstWarehouse ():
    vGolf = []
    for i in range (5):
        section = []
        partID = input("Enter Part's ID : ")
        part = input ("Enter Part : ")
        amount = input ("Enter Amount : ")

        section.append(partID)
        section.append(part)
        section.append(amount)

        vGolf.append(section)
        vGolf.sort()
        print("\n")

    writeFile('vGolf.txt',vGolf,section)

    return vGolf

def secondWarehouse ():
    vGolf_R = []
    for i in range (5):
        section = []
        partID = input("Enter Part's ID : ")
        part = input ("Enter Part : ")
        amount = input ("Enter Amount : ")

        section.append(partID)
        section.append(part)
        section.append(amount)

        vGolf_R.append(section)
        vGolf_R.sort()
        print("\n")

    writeFile('vGolf_R.txt',vGolf_R,section)

    return vGolf_R

def thirdWarehouse():
    vGolf_G = []
    for i in range (5):
        section = []
        partID = input("Enter Part's ID : ")
        part = input ("Enter Part : ")
        amount = input ("Enter Amount : ")

        section.append(partID)
        section.append(part)
        section.append(amount)

        vGolf_G.append(section)
        vGolf_G.sort()
        print("\n")

    writeFile('vGolf_G.txt',vGolf_G,section)

    return vGolf_G

#########################################################################################

### Printing Parts' Amount below 10

# Function of condition
def checkCondition(line):
    if line [-2:] < '10':
        print (line)
    else:
        print ('Amount Sufficient')
    return checkCondition

def itemBelow_vGolf ():
    vGolffile = open('vGolf.txt','r')
    for line in vGolffile:
        line = line.rstrip()

        checkCondition(line)
    vGolffile.close()
    
    return itemBelow_vGolf

def itemBelow_vGolf_R () :
    vGolf_Rfile = open ('vGolf_R.txt','r')
    for line in vGolf_Rfile:
        line = line.rstrip()
     
        checkCondition(line)
    vGolf_Rfile.close()
    
    return itemBelow_vGolf_R

def itemBelow_vGolf_G ():
    vGolf_Gfile = open ('vGolf_G.txt','r')
    for line in vGolf_Gfile:
        line = line.rstrip ()
        
        checkCondition(line)
    vGolf_Gfile.close()
    
    return itemBelow_vGolf_G

###########################################################################################

### Checking part which are body section from three warehouses
## Check Function
def checkFunction(fileNameRead, fileNameWrite, types, itemCodeCaps, itemCodeNCaps):
    file = open(fileNameRead,'r')

    for line in file:
        if line.startswith(itemCodeCaps) or line.startswith (itemCodeNCaps):
            file = open(fileNameWrite,types)
            file.write(line)
            file.write('\n')
            file.close()    # Close File Write
        print(line)
    file.close()    # Close File Read

    return checkFunction

### Body Section

def bodySection ():

    writeFileName = 'Body_Section.txt'  # File Name to write into

    #Get the Steering item from each warehouse to Body_Section text file
    checkFunction('vGolf.txt', writeFileName, 'w', 'SV5', 'sv5')
    checkFunction('vGolf_R.txt', writeFileName, 'a','SVR5', 'svr5')
    checkFunction('vGolf_G.txt', writeFileName, 'a','SVG5', 'svg5')

    return bodySection

#################################

### Engine Section

def engineSection () :

    writeFileNameR = 'Engine_Section.txt'

    #Get Air Condition and Multi-Cylinder item from each warehouse to Engine_Section text file
    checkFunction('vGolf.txt', writeFileNameR, 'w', 'MCEV3', 'mcev3')
    checkFunction('vGolf.txt', writeFileNameR, 'a', 'ACEV4', 'acev4')
    checkFunction('vGolf_R.txt', writeFileNameR, 'a', 'MCEVR3', 'mcevr3')
    checkFunction('vGolf_R.txt', writeFileNameR, 'a', 'ACEVR4', 'acevr4')
    checkFunction('vGolf_G.txt', writeFileNameR, 'a', 'MCEVG3', 'mcevg3')
    checkFunction('vGolf_G.txt', writeFileNameR, 'a', 'ACEVG4', 'acevg4')

    return engineSection

#######################################

### Transmission Section

def transmissionSection ():

    writeFileNameT = 'Transmission_Section'

    # Get Clutch and Gear Box from each warehouse to Transmission_Section text file
    checkFunction('vGolf.txt', writeFileNameT, 'w', 'GBV1', 'gbv1')
    checkFunction('vGolf.txt', writeFileNameT, 'a', 'CV2', 'cv2')
    checkFunction('vGolf_R.txt', writeFileNameT, 'a', 'GBVR1', 'gbvr1')
    checkFunction('vGolf_R.txt', writeFileNameT, 'a', 'CVR2', 'cvr2')
    checkFunction('vGolf_G.txt', writeFileNameT, 'a', 'GBVG1', 'gbvg1')
    checkFunction('vGolf_G.txt', writeFileNameT, 'a', 'CVG2', 'cvg2')

    return transmissionSection

###########################################################################################

#### Print Each Section's Parts and Amount 

## Function of printing
def printFunction(fileName):
    file = open(fileName,'r')
    for line in file:
        line = line.rstrip()
        print(line)
    file.close()
    return fileName

def printBodySection():
    printFunction('Body_Section.txt')

    return printBodySection

def printEngineSection ():
    printFunction('Engine_Section.txt')

    return printEngineSection

def printTransmissionSection():
    printFunction('Transmission_Section.txt')

    return printTransmissionSection

###########################################################################################

### Supllier INFO

def supplierInfo ():
    supplierList = []
    for i in range (3):
        
        supplies = []
        name = input ("Enter Name : ")
        supplies.append('Name :')
        supplies.append(name)
        
        number = input ("Enter Phone Number : ")
        supplies.append('Phone Number : ')
        supplies.append(number)
        
        partID = input ("Supplied Part's ID : ")
        supplies.append("Part's ID : ")
        supplies.append(partID)
        
        numberSupplied = input("Enter Supplied Amount : ")
        supplies.append('Total Supplied Amount : ')
        supplies.append(numberSupplied)

        supplierList.append(supplies)

    writeFile('Supplier.txt', supplierList, supplies)   ## Function of writing file

    return supplierInfo

###########################################################################################

### Recording for supplying more than one part from suppliers

def supplierMoreOne ():

    inputs = int (input("Enter 1 to record, 0 to end : "))
    while True :
        if inputs == 0 :
            break
        else :
            supplied = []
            supplies = []

            supplier = input ("Enter Supplier Name : ")
            suppliedPartID = input ("Parts Supplied : ")

            supplies.append(supplier)
            supplies.append(suppliedPartID)

            supplied.append(supplies)
            inputs = int (input("Enter 1 to record, 0 to end : "))
            
        supplyMore_File = open ('Supplied_More_1.txt','a')
        for supplies in supplied:
            for item in supplies:
                supplyMore_File.write(item)
                supplyMore_File.write("\t")
            supplyMore_File.write("\n")
        supplyMore_File.close()
        
    return supplierMoreOne

############################################################################################

#### Update Parts ####

## Fucntion of finding condition of each item
def updateCondition(itemCode, inputItem, fileName):
    
    file = open(fileName, 'r')
    data = file.readlines()
    newData = []
    for line in data:
        line = line.rstrip()
        newLine = line.rsplit("\t")
        if(newLine [0] == itemCode):
            newLine [2] = inputItem
        newData.append(newLine)

        print(line)
        
    writeFile(fileName, newData, data)
    
    return updateCondition

### vGolf (firstWarehouse)

name = 'vGolf.txt'

def updateGearBox ():

    updateGearBox = input ("Enter Gear Box Amount : ")

    updateCondition('GBV1', updateGearBox, name)

    return updateGearBox

def updateClutch ():

    updateClutch = input ("Enter Clutch Amount : ")

    updateCondition('CV2', updateClutch, name)
    
    return updateClutch
        
def updateMultiCylinderEngine ():

    updateMultiCylinderEngine = input ("Enter Multi-Cylinder Engine Amount : ")

    updateCondition('MCEV3', updateMultiCylinderEngine, name)
    
    return updateMultiCylinderEngine

def updateAirCooledEngine ():

    updateAirCooledEngine = input ("Enter Air-Cooled Engine Amount : ")

    updateCondition('ACEV4', updateAirCooledEngine, name)
    
    return updateAirCooledEngine

def updateSteering () :
    
    updateSteering = input ("Enter Steering Amount : ")

    updateCondition('SV5', updateSteering, name)
    
    return updateSteering

###########################

### Update vGolf_R (second Warehouse)

nameR = 'vGolf_R.txt'

def updateGearBox_R():

    updateGearBox_R = input ("Enter Gear Box_R Amount : ")

    updateCondition('GBVR1', updateGearBox_R, nameR)
    
    return updateGearBox_R

def updateClutch_R():

    updateClutch_R = input ("Enter Clutch_R Amount : ")

    updateCondition('CVR2', updateClutch_R, nameR)
    
    return updateClutch_R

def updateMultiCylinderEngine_R():

    updateMultiCylinderEngine_R = input ("Enter Multi-Cylinder_R Engine Amount : ")

    updateCondition('MCEVR3', updateMultiCylinderEngine_R, nameR)
    
    return updateMultiCylinderEngine_R

def updateAirCooledEngine_R():

    updateAirCooledEngine_R = input ( " Enter Air-Cooled_R Engine Amount : ")

    updateCondition('ACEVR4', updateAirCooledEngine_R, nameR)
    
    return updateAirCooledEngine_R

def updateSteering_R():

    updateSteering_R = input ("Enter Steering_R Amount : ")

    updateCondition('SVR5', updateSteering_R, nameR)
    
    return updateSteering_R

##############################################

#### Update vGolf_G (thirdWarehouse)

nameG = 'vGolf_G.txt'

def updateGearBox_G():

    updateGearBox_G = input ("Enter Gear Box_G Amount : ")

    updateCondition('GBVG', updateGearBox_G, nameG)
    
    return updateGearBox_G

def updateClutch_G():

    updateClutch_G = input ("Enter Clutch_G Amount : ")

    updateCondition('CVG2', updateClutch_G, nameG)

    return updateClutch_G

def updateMultiCylinderEngine_G():

    updateMultiCylinderEngine_G = input ("Enter Multi-Cylinder_G Engine Amount : ")
    
    updateCondition('MCEVG3', updateMultiCylinderEngine_G, nameG)

    return updateMultiCylinderEngine_G

def updateAirCooledEngine_G():

    updateAirCooledEngine_G = input ( " Enter Air-Cooled_G Engine Amount : ")

    updateCondition('ACEVG4', updateAirCooledEngine_G, nameG)
    
    return updateAirCooledEngine_G

def updateSteering_G():

    updateSteering_G = input ("Enter Steering_G Amount : ")

    updateCondition('SVG5', updateSteering_G, nameG)
    
    return updateSteering_G

###############################################################################################

## Create new part in warehouses

## Create Function
def createFunction(fileName):
    section = []

    partID = input ("Enter Part's ID : ")
    part = input ("Enter Part : ")
    amount = input ("Enter Amount : ")

    section.append(partID)
    section.append(part)
    section.append(amount)

    file = open(fileName,'a')
    for item in section:
        file.write(item)
        file.write('\t')
    file.write('\n')
    file.close()
    
    return createFunction

def newPart ():
    inputs = int(input("Enter 1 to add new Part, 0 to end : "))
    while True :
        if inputs == 0 :
            break
        else :
            createFunction('vGolf.txt')
            
            inputs = int(input("Enter 1 to continue add new Part, 0 to end : "))
            
    return newPart

def newPart_R ():
    inputs = int(input("Enter 1 to add new Part, 0 to end : "))
    while True :
        if inputs == 0 :
            break
        else :
            createFunction('vGolf_R.txt')

            inputs = int(input("Enter 1 to continue add new Part, 0 to end : "))
            
    return newPart_R

def newPart_G ():
    inputs = int(input("Enter 1 to add new Part, 0 to end : "))
    
    while True :
        if inputs == 0 :
            break

        else :
            createFunction('vGolf_G.txt')

            inputs = int(input("Enter 1 to continue add new Part, 0 to end : "))

    return newPart_G

###########################################################################################

### Search Function

def searchFunction(fileName):
    try:
        file = open(fileName,'r')
        search = input("Search : ")
        for line in file:
            line = line.rstrip()
            if search.lower() in line.lower():
                print(line)
                break;
            else:                
                print('Item Not Found')
                break;
        file.close()
        
    except:
        print('File Not Found')
        exit()
    
    return searchFunction

def searchvGolf():
    searchFunction('vGolf.txt')
    
    return searchvGolf

def searchvGolf_R():
    searchFunction('vGolf_R.txt')
    
    return searchvGolf_R

def searchvGolf_G():
    searchFunction('vGolf_G.txt')
    
    return searchvGolf_G

def searchSupplier():
    searchFunction('Supplier.txt')

    return searchSupplier

def searchSuppliedMore():
    searchFunction('Supplied_More_1.txt')

    return searchSuppliedMore

###############################################################################

#### Print FUNCTION
def printFunction(fileName):
    file = open(fileName,'r')
    for line in file:
        line = line.rstrip()
        print(line,"\n")
    file.close()
    
    return printFunction

def printvGolfRecord():
    printFunction('vGolf.txt')
    
    return printvGolfRecord

def printvGolf_RRecord ():
    printFunction('vGolf_R.txt')
    
    return printvGolf_RRecord

def printvGolf_GRecord ():
    printFunction('vGolf_G.txt')
    
    return printvGolf_GRecord

def printSupplierMoreOne():
    printFunction('Supplied_More_1.txt')
    
    return printSupplierMoreOne

################################################################################
################################################################################

### MENU FUNCTION

def menu_0 ():
    print ("1. To add new parts ")
    print ( "\t", "A. vGolf" )
    print ( "\t", "B. vGolf_R" )
    print ( "\t", "C. vGolf_G" )
    print ("2. To update parts ")
    print ( "\t", "A. vGolf" )
    print ( "\t" "\t", "a. Gear Box" )
    print ( "\t" "\t", "b. Clutch " )
    print ( "\t" "\t", "c. Multi-Cyclinder Engine " )
    print ( "\t" "\t", "d. Air-Cooled Engine " )
    print ( "\t" "\t", "e. Steering ")
    print ( "\t", "B. vGolf_R" )
    print ( "\t" "\t", "a. Gear Box" )
    print ( "\t" "\t", "b. Clutch " )
    print ( "\t" "\t", "c. Multi-Cyclinder Engine " )
    print ( "\t" "\t", "d. Air-Cooled Engine " )
    print ( "\t" "\t", "e. Steering ")
    print ( "\t", "C. vGolf_G" )
    print ( "\t" "\t", "a. Gear Box" )
    print ( "\t" "\t", "b. Clutch " )
    print ( "\t" "\t", "c. Multi-Cylinder Engine " )
    print ( "\t" "\t", "d. Air-Cooled Engine " )
    print ( "\t" "\t", "e. Steering ")



    choice = int(input("Enter 1 to record new part , 2 to Update Part : "))
    if choice == 1 :
        alphabet_0 = input ("Enter Which Warehouse : ")
        if alphabet_0 == 'A' or alphabet_0 == 'a' :
            newPart()
        elif alphabet_0 == 'B' or alphabet_0 == 'b':
            newPart_R()    
        else :
            newPart_G()   
    else :
        alphabet_1 = input ("Enter Which Warehouse : ")
        if alphabet_1 == 'A' or alphabet_1 == 'a':
            part = input ("Select Which Part to Update : ")
            if part == 'a' or part == 'A':
                updateGearBox()
            elif part == 'b' or part == 'B':
                updateClutch()
            elif part == 'c' or part == 'C':
                updateMultiCylinderEngine()
            elif part == 'd' or part == 'D':
                updateAirCooledEngine ()
            else :
                updateSteering()
        elif alphabet_1 == 'B' or alphabet_1 == 'b':
            part = input ("Select Which Part to Update : ")
            if part == 'a' or part == 'A':
                updateGearBox_R()
            elif part == 'b' or part == 'B':
                updateClutch_R()
            elif part == 'c' or part == 'C':
                updateMultiCylinderEngine_R()
            elif part == 'd' or part == 'D':
                updateAirCooledEngine_R ()
            else :
                updateSteering_R()
        else :
            part = input ("Select Which Part to Update : ")
            if part == 'a' or part == 'A':
                updateGearBox_G()
            elif part == 'b' or part == 'B':
                updateClutch_G()
            elif part == 'c' or part == 'C':
                updateMultiCylinderEngine_G()
            elif part == 'd' or part == 'D':
                updateAirCooledEngine_G ()
            else :
                updateSteering_G()

def menu():

    print ( ' WELCOME TO VOLKSWAGEN MANUFACTURE ! ')
    print ( ' Please Choose Your Option ')

    print ( '1. Insert Parts To Warehouse ')
    print ( "\t", "A. vGolf" )
    print ( "\t", "B. vGolf_R" )
    print ( "\t", "C. vGolf_G" )
	
    print ( "2. Update Parts or Insert New Parts " )
	
    print ( "3. Supplier Information ")
	
    print ( "4. Insert Suppliers supplied More Than One Part ")
	
    print ( "5. Check Suppliers Supplied Part's Quantity")									### Print who supplies more than one part 
	
    print ( "6. Check Section From Warehouses")	## Printing items in text files							### Categories Parts into Sections
    print ( "\t" "A. Body Section " )
    print ( "\t" "B. Engine Section")
    print ( "\t" "C. Transmission Section ")
	
    print ( "7. Print Sections")
    print ( "\t" "A. Body Section ")
    print ( "\t" "B. Engine Section ")
    print ( "\t" "C. Transmission Section ")
	
    print ( "8. Check The Amount of Parts In Each Warehouse ")
    print ( "\t" "A. vGolf " )
    print ( "\t" "B. vGolf_R" )
    print ( "\t" "C. vGolf_G" )
    
    print ( "9. Check Unefficient Quantity ")											### part that below 10 
    print ( "\t" "A. vGolf " )
    print ( "\t" "B. vGolf_R" )
    print ( "\t" "C. vGolf_G" )
	
    print ( "10. Search ")
    print ( "\t" "A. vGolf " )
    print ( "\t" "B. vGolf_R" )
    print ( "\t" "C. vGolf_G" )
    print ( "\t" "D. Supplier Information " )
    print ( "\t" "E. Suppliers Supplied More Than 2 Parts " )
	
    print ( "11. Exit" )


    while True :
        toContinue = int(input("Enter 1 to continue , 0 to end : "))
        if toContinue == 0:
            break
        else:
            choice = int(input("Enter Your Option : "))

            if choice == 1:
                alphabet = input("Select Which Warehouse : ")
                if alphabet == 'A' or alphabet == 'a':
                    firstWarehouse()
                elif alphabet == 'B' or alphabet == 'b':
                    secondWarehouse ()
                else:
                    thirdWarehouse()

            elif choice == 2 :
                menu_0()

            elif choice == 3 :
                supplierInfo()

            elif choice == 4 :
                supplierMoreOne()

            elif choice == 5 :
                printSupplierMoreOne()

            elif choice == 6 :
                alphabet_2 = input ("Check Which Section : ")
                if alphabet_2 == 'A' or alphabet_2 == 'a':
                    bodySection()
                elif alphabet_2 == 'B' or alphabet_2 == 'b':
                    engineSection()
                else :
                    transmissionSection()

            elif choice == 7:
                alphabet_3 = input ("To Print Which Section : ")
                if alphabet_3 == 'A' or alphabet_3 == 'a':
                    printBodySection()
                elif alphabet_3 == 'B' or alphabet_3 == 'b':
                    printEngineSection()
                else:
                    printTransmissionSection()

            elif choice == 8:
                alphabet_4 = input ("Check Which Warehouse : ")
                if alphabet_4 == 'A' or alphabet_4 == 'a':
                    printvGolfRecord()
                elif alphabet_4 == 'B' or alphabet_4 == 'b':
                    printvGolf_RRecord()
                else:
                    printvGolf_GRecord()

            elif choice == 9:
                alphabet_5 = input ("Check Which Warehouse : ")
                if alphabet_5 == 'A' or alphabet_5 == 'a':
                    itemBelow_vGolf()
                elif alphabet_5 == 'B' or alphabet_5 == 'b':
                    itemBelow_vGolf_R()
                else:
                    itemBelow_vGolf_G()

            elif choice == 10 :
                alphabet_6 = input ("Select Section to Search : ")
                if alphabet_6 == 'A' or alphabet_6 == 'a':
                    searchvGolf()
                elif alphabet_6 == 'B' or alphabet_6 == 'b':
                    searchvGolf_R()
                elif alphabet_6 == 'C' or alphabet_6 == 'c':
                    searchvGolf_G()
                elif alphabet_6 == 'D' or alphabet_6 == 'd':
                    searchSupplier()
                else :
                    searchSuppliedMore()

            else :
                print (" THANK YOU !! ")
                exit ()
menu()
