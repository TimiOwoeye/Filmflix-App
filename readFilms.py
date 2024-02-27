from connect import * 

# create a subroutine
def read_films():
    try:  # select all records from the table
        dbCursor.execute("SELECT * FROM tblFilms")

        # fetchall(): fetehes all the the selected records
        rows = dbCursor.fetchall()# row holds alll fetched records

        # loop through all the records in the row variable 
        for aRecord in rows:
            # print all record 
            print(aRecord)
    except sql.OperationalError as e:
        print(f"Records not found: {e}")
if __name__ == "__main__":
    read_films()

