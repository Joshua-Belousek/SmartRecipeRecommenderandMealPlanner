import csv
import json

def read_ingredients_csv(file):
    with open(file, mode = 'r') as file: #open the file on reading mode
        read = csv.reader(file)
        next(read) # skip the header of the file
        for row in read:
            print(f"Name:{row[0]}, Quantity: {row[1]}, Unit:{row[2]}")

#function to read Json file
def read_Json(file):
    with open(file, mode='r') as file:
        data = json.load(file)

read_ingredients_csv('ingredients.csv')
