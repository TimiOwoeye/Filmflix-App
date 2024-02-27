from connect import * 
import logging
import time
filename = __name__
logging.basicConfig(filename=r"Week_10\Pt9_10DBOps\file.log", level=logging.DEBUG)

# create a subroutine
def search():
    try:
        field = input("Would you like to search by MemberID or Firstname or Lastname or Email? ")
        if field == "MemberID":
            idInput = input("Enter MemberID: ")
            dbCursor.execute(f"SELECT * FROM members WHERE MemberID = {idInput}")
            row = dbCursor.fetchone()
            if row == None:
                print(f"No record with {idInput} exists in the table: ")
                logging.warning(f"On {time.asctime()}, file is {filename}, user entered {idInput} as {field}")

                
            else:
                for aRecord in row:
                    print(aRecord)
        elif field == "Firstname" or field == "Lastname" or field == "Email":
            searchInput = input(f"Enter search field for {field}: ")
            dbCursor.execute(f"SELECT * FROM members WHERE {field} LIKE '%{searchInput}%'")
            rows = dbCursor.fetchall()
            if rows == None:
                print(f"No record with field {field} Matching '{searchInput}' in the table ")
            else:
                for records in rows:
                    print(records)
        else:
            print(f"Invalid search filed {field}")
    except sql.OperationalError as e:
        print(f"No Database or table found: {e}")
if __name__ == "__main__":
    search()
