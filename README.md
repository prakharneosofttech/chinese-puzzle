# Chinese Puzzle

## The puzzle to count the number of rabbits and chickens based on heads and legs count.

## Technology Used

- FastAPI
- Python3.8

## Pre-requisite for running the application
- You should have Python3.8 installed
- Pip version should 21.3.1+
- Shell system to run the test file (Optional)

## How to run the application
- Clone the repo
- Install the required packages by `pip install -r requirements.txt`
- Start the local server by `uvicorn main:app`
- Run run.sh file by `./run.sh` (make sure the file has executable permissions)
- Look for the response of the API with multi test cases in the terminal

## How to run the tests
- Make sure you have all the packages available in requirements.txt
- Run `pytest` command in the terminal and see the result of test cases.

Optionally 
- You can run `127.0.0.1:8000/get_count?head_count=10&leg_count=22` directly in your browser

Author,
Prakhar
