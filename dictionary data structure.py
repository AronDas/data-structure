student_id = {
    "id_1" : {"name": "Aron", "class": "7", "subjects": "French, math, science"},
    "id_2" : {"name": "Max", "class": "7", "subjects": "French, math, science"},
    "id_3" : {"name": "Arthur", "class": "7", "subjects": "French, math, science"},
    "id_4" : {"name": "Aron", "class": "7", "subjects": "French, math, science"},
}

result = {}
seen_keys = []

for student_id, Details in student_id.items():
    unique_key = (Details["name"], Details["class"], Details["subjects"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = Details

for k, v in result.items():
    print(k, ":", v)
