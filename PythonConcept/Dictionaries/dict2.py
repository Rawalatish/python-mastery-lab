student = {"name": "Alice",
           "age": 58,
           "courses": ["Math", "CS"]
           }

nn =(student.values())
print(nn)                           # op=> dict_values(['Alice', 58, ['Math', 'CS']])
mm = list(student.values())
print(mm)                          # op => ['Alice', 58, ['Math', 'CS']]


oo = tuple(student.keys())
print(oo)                           # ('name', 'age', 'courses')


pp = list(student.items())
print(pp)                           # [('name', 'Alice'), ('age', 58), ('courses', ['Math', 'CS'])]
