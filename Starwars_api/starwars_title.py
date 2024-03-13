#!/usr/bin/python3

import requests
import json
import sys

# Error check the arguments
if len(sys.argv) != 2:
    print("The script requires 1 argument to work")
    sys.exit(1) # Exit with error status

# Add an args for movie ID
movie_id = sys.argv[1]

# Define the API endpoint URL
url = 'https://swapi.py4e.com/api/films/' + movie_id

# Make a get rquest to the API endpoint
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the response to json format
    data = response.json()
    
    # Process the data as needed
    print(json.dumps(data, indent=4))
else:
    # Print an error message if the request was unsuccessful
    print("Error:", response.status_code)
