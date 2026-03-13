def mean_calculation(data,category):
    value = 0
    for index in range(len(data)):
        value += data[index][category]
    return value/len(data)

def max_age(data):
    max = 0
    for index in range(len(data)):
        if max < data[index]["edad"]:
            max = data[index]["edad"]
    return max

def min_age(data):
    min = 100
    for index in range(len(data)):
        if min > data[index]["edad"]:
            min = data[index]["edad"]
    return min

def count_career(data):
    career = {}
    for index in range(len(data)):
        topic = data[index]["carrera"]
        if topic in career:
            career[topic] += 1
        else:
            career[topic] = 1
    return career

def filter_age(data, min_age):
    data_filter = []
    for student in data:
        if student["edad"] >= min_age:
            data_filter.append(student)
    return data_filter

def filter_average(data, average):
    data_filter = []
    for student in data:
        if student["promedio"] >= average:
            data_filter.append(student)
    return data_filter

def filter_career(data, career):
    data_filter = []
    for student in data:
        if student["carrera"] == career:
            data_filter.append(student)
    return data_filter

def sorted_data(data, category):
    list = sorted(data, key= lambda student: student[category])
    return list
