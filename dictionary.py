student_data = {

'id1': {

'name': 'Sara',

'class': 'V',

'subject_integration': ['english', 'math', 'science']

},

'id2': {

'name': 'David',

'class': 'V',

'subject_integration': ['english', 'math', 'science']

},

'id3': {

'name': 'Sara',

'class': 'V',

'subject_integration': ['english', 'math', 'science']

},

'id4': {

'name': 'Surya',

'class': 'V',

'subject_integration': ['english', 'math', 'science']

}

}

result = {}

seen = set()

for key, value in student_data.items():

# Convert dict to a hashable tuple so we can check for duplicates

entry = (

value['name'],

value['class'],

tuple(value['subject_integration'])

)


if entry not in seen:

seen.add(entry)

result[key] = value

print(result)