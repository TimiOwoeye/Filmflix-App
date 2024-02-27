from connect import * 

# create a subroutine
def insert_films():
    # create an empty list 
    films = []
    # ask for user input (MemberID, Firstname, Lastname and Email)
    # MemberID is an auto increment field and does not require input   
    title = input("Enter the title of the film: ")
    yearReleased = int(input("Enter the year released: "))
    rating = input("Enter the rating: ")
    duration = int(input("Enter the duration (in minutes): "))
    genre = input("Enter the genre: ")



    print(f"Data: {title,yearReleased,rating, duration,genre}")
    # append data Firstname, Lastname and Email
    films.append(title)
    films.append(yearReleased)
    films.append(rating)
    films.append(duration)
    films.append(genre)
    print(f"The films list {films}")

    "INSERT INTO members VALUES(NULL, 'A','B','C')"
    "INSERT INTO members (Firstname, Lastname , Email) VALUES( 'A','B','C')"

    try:
        # dbCursor.execute("INSERT INTO members VALUES(NULL,?,?,?)", members) # Values from the list
        # or 
        # values directly from variables
        # dbCursor.execute("INSERT INTO members VALUES(NULL, ?,?,?)", (fName,lName,email))
    
        dbCursor.execute("INSERT INTO tblfilms (title, yearReleased, rating, duration, genre) VALUES (?, ?, ?, ?, ?)",
              (title, yearReleased, rating, duration, genre))
        dbCon.commit() # make the changes permanent 
        print(f"{genre} inserted in the Table")
    except sql.OperationalError as e:
        dbCon.rollback()
        print(f"Insert failed: {e}")
if __name__== "__main__":
    insert_films()