from pymongo import MongoClient

#Establish the mongodb connection with client                       # CURD Apply by collections

client = MongoClient("mongodb://localhost:27017")

# To create database using client

student_db = client['student_db']

# To create collection using database

student_collection = student_db["student_collection"]

# To insert the student information using collection

count = 1
for i in range(1, 5):
    print(f"Enter student {count} :- ")
    count += 1
    student_collection.insert_one({
    "Name": input("Enter your Name:- "),
    "E-mail": input("Enter your E-mail:- "),
    "Mobile" : int(input("Enter your mobile no.:- ")),
    "Department" : input("Enter your Department:- "),
    "Interested_technology": input("Enter your interested technology:- ")})

    
# To add the multiple document in list 

'''student_record = [
    {
        "name": "Aman",
        "age": 21,
        "email": "aman@example.com",
        "city": "Delhi"

    },
    {
        "name": "Amar",
        "age": 25,
        "email": "priya@example.com",
        "city": "Mumbai"
    },
    {
        "name": "Akhil",
        "age": 21,
        "email": "ravi@example.com",
        "city": "Bangalore"
    },
    {
        "name": "Dharamveer",
        "age": 22,
        "email": "neha@example.com",
        "city": "Kolkata"
    },
    {
        "name": "Divyansh",
        "age": 22,
        "email": "arjun@example.com",
        "city": "Chennai"
    }
]
student_collection.insert_many(student_record)'''

"""student_collection.insert_many([
    {
        "name": "Aman",
        "age": 21,
        "email": "aman@example.com",
        "city": "Delhi"

    },
    {
        "name": "Amar",
        "age": 25,
        "email": "priya@example.com",
        "city": "Mumbai"
    },
    {
        "name": "Akhil",
        "age": 21,
        "email": "ravi@example.com",
        "city": "Bangalore"
    },
    {
        "name": "Dharamveer",
        "age": 22,
        "email": "neha@example.com",
        "city": "Kolkata"
    },
    {
        "name": "Divyansh",
        "age": 22,
        "email": "arjun@example.com",
        "city": "Chennai"
    }
])"""

# To Remove the student information from friendlist

student_collection.delete_one({'name' : 'Dharamveer'})
student_collection.delete_many({'name' : 'Aman'})

# Name, E-mail, Mobile, department, interested technology