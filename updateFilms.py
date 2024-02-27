from connect import * 

# create a subroutine
def update_films():
    #use MemberID is a primary and a unique field to update a record
       #  the id of the record to be updated 
    idField = input("Enter the FilmID to update a record: ")

    # select all fields for update 
    genre = input("Enter Genre: ").title()
    year = input("Enter Year: ").title()
    rating = input("Enter Rating: ").title()

    # add quotes to field value 
    genre = "'"+genre+"'"
    year = "'"+year+"'"
    rating = "'"+rating+"'"   
    
    try: # UPDATE members SET Firstname = "James" WHERE MemberID = 1/2/3/4....
        dbCursor.execute(f"UPDATE films SET Genre = {genre}, Year = {year}, Rating = {rating} WHERE FilmID = {idField} ")
        dbCon.commit()
        print(f"{idField} Updated in the films table ")
    except sql.OperationalError as e:
        print(f"Update failed: {e}")

if __name__ == "__main__":
    update_films()

