import sqlite3


connection = sqlite3.connect('student.db') #file name
print('Database opened successfully')

TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " + STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER); ")

print("table created successfully.")

##insert new record
connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", "
                   + STUDENT_PHONE + ") VALUES ( 'MOHIT', 'DIT', " "'DEHRADUN, UTTARAKHAND', 9760630296); ")
connection.commit()

#Dynamically adding values to database
for i in range(2):
    name = input('enter your name')
    college = input('enter your college')
    address = input('enter your address')
    phone = input('enter your phone number')
    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " + STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " + STUDENT_PHONE + ") VALUES ('"+name+"', '"+college+"', " + "'"+address+"', "+phone+" ); ")

connection.commit()

#retrieve record
cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")

for row in cursor:
    print("student id is: ", row[0])
    print("student name is: ", row[1])
    print("student college is: ", row[2])

connection.close()