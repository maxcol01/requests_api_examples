import requests
from html import unescape
import csv

# Prepare the request
URL: str = "https://opentdb.com/api.php"

def ask_question() -> str:
    amount = input("How many questions do you want ?: ")
    difficulty = input("What is the level of difficulty (easy/medium/difficult)?: ")
    return amount, difficulty

amount, difficulty = ask_question()

PARAMETERS: dict = {
    "amount" : amount,
    "difficulty" : difficulty,
    "category": 18
}

# make the request

response = requests.get(URL, params=PARAMETERS)
data = response.json()

# Prepare the data
question_list: list = [unescape(item["question"]) for item in data["results"]]
answer_list: list = [unescape(item["correct_answer"]) for item in data["results"]]


# Prepare the data as a list of dictionaries
data_rows: list[dict] = [{"Questions": question, "Answers": answer} for question, answer in zip(question_list, answer_list)]


# Store in a CSV file
with open("Trivia.csv", mode="w", newline="") as file:
    fieldnames: list = ['Questions', 'Answers']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data_rows)


