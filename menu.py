import readFilms, addFilms, updateFilms, deleteFilms, searchReport
def read_file():
    try:
        with open("py.Project/menuOptions.txt") as fileRead:
            fr = fileRead.read()
        return fr
    except FileNotFoundError as nf:
        print(f"Check {nf}")

# create the menu function 
def films_menu():
    option = 0 # initialise theoption variable with an integere value
    optionsList = ["1","2","3","4","5","6"]

    # assign the  read_file() function to the menuChoices variable 
    filmChoices =  read_file()

    # create a while loop to repeat the code within the bod of while condition
    while option not in optionsList:
        print(filmChoices) # call/invoke read_file() function to the menuChoices variable 

        # re-assign the valeu of the option variable with the input function 
        option = input("Enter an option from the Menu choice above: ")

        # check if the input from the option variable match any of the options 
        # in the optionsList(["1","2","3","4","5","6"]) 
        if option not in optionsList:
            # if the condition above is true execute the code below
            print(f"{option} is not a valid choice! ")
    return option


mainProgram = True # Boolean variabe to toggle True/False

while mainProgram: #While True
    # assign the members_menu() function to the mainMenu variable 
    mainMenu = films_menu()

    if mainMenu == "1":
        readFilms.read_films()
    elif mainMenu == "2":
        addFilms.insert_films()
    elif mainMenu == "3":
        updateFilms.update_films()
    elif mainMenu == "4":
        deleteFilms.delete_films()
    elif mainMenu == "5":
        searchReport.search()
    else:
        input("Press Enter key to exit the program: ")
        mainProgram = False
        

    
