import json
import sys
import numpy as np
with open("quiz_files/output.json", "r") as f:
    file = json.load(f)
count = len(file) - 1
opts = ["A", "B", "C", "D"]
# list of dictionaries, two dictionary keys (question and choices)
# choices.values() is a list.
def show_question(i):
    for key, val in file[i].items():
        if key == "question":
            print(val)
        if key == "choices":
            for choice in val:
                for keys in choice.keys():
                    if keys in opts:
                        print(f"{keys}. {choice.get(keys)}")
                    else:
                        answer = choice.get(keys)
    return answer

def quiz(total):
    score = 0
    queue = []
    for questions in range(total):
        qran = np.random.randint(0, count)
        result = show_question(qran)
        while True:
            answer = input("Enter answer choice: ")
            if len(answer) == 1:
                if ord(answer) in range(65, 69):
                    if answer == result or answer == result.lower():
                        print("Correct!")
                        score += 1
                        break
                    else:
                        print("Incorrect.")
                        break
                elif ord(answer) in range(49, 53):
                    if opts[int(answer)-1] == result:
                        print("Correct!")
                        score += 1
                        break
                    else:
                        print("Incorrect.")
                        break
            else:
                print("Not an answer, try again!")
                pass
        queue.append(qran)

    print(f"Final score: {score/ total*100:.2f}%")
if __name__ == "__main__":
    total = int(sys.argv[1])
    quiz(total)

'''
TODO:
Make pywebview gui.
'''
