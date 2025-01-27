import re
import json
questions = {}

with open("out.txt", "r", encoding="utf8") as f:
    text = f.read()
    out = re.finditer(r"\d[0-9.]*\s(\w.*[?.:])\W+([A-Z].*)\W+([A-Z].*)\W+([A-Z].*)\W+([A-Z].*)\W+(Answer:\W[A-Z])", text, flags=re.MULTILINE)
    
    for matches in out:
        match = matches.groups()
        answers = match[5].split(':')
        choices = []
        
        for i in range(1, 5):
            choice = match[i].split(".")
            choices.append({choice[0].strip(): choice[1].strip()})
        

        choices.append({answers[0].strip(): answers[1].strip()})
        

        if match[0] in questions:
            questions[match[0]].extend(choices)
        else:
            questions[match[0]] = choices


final_output = []
for question, choices in questions.items():
    final_output.append({"question": question, "choices": choices})


with open('output.json', 'w') as f:
    json.dump(final_output, f, indent=4)
