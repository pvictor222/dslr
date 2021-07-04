"""
    1.  Removing the names
    2.  Replacing the hands by 0 (right) or 1 (left)
    3.  Split the date of birth in 3 variables : day, month and year
"""

def data_cleaning(data):
    data[0].append("Year")
    data[0].append("Month")
    data[0].append("Day")
    for i in data[1:]:
        i.pop(2)
        i.pop(2)
        if (i[3] == "Left"):
            i[3] = 1
        else:
            i[3] = 0
        birthday = i[2].split('-')
        i.append(birthday[0])
        i.append(birthday[1])
        i.append(birthday[2])