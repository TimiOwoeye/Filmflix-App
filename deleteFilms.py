from connect import * 

# create a subroutine
def delete_films():

    try:
        #use MemberID: is a primary and a unique field to delete a record
       # the id of the record to be deleted 
        idField = input("Enter the FilmID to delete a record: ")

        # select a record using MemberID from the table
        dbCursor.execute(f"SELECT * FROM tblfilms WHERE filmID = {idField} ")

        row = dbCursor.fetchone() # use the fetchone() to fetch the selected record
        #None: A singleton object used to check/signal if value is absent

        if row == None: # row is the record returned based on the specific MemberID
            print(f"No record wih the FilmID {idField} exists")
        
        else:
            dbCursor.execute(f"DELETE FROM tblfilms WHERE filmID = {idField} ")
            dbCon.commit()
            print(f"Record {idField} deleted")
    
    except sql.OperationalError as e:
        print(f"No Database or table found: {e}")
    
if __name__ == "__main__":
    delete_films()

        
 