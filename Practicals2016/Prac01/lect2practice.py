group_number = 0
member_age = []
total_age = 0
age = 0
while group_number <= 0:
    group_number = int(input('Please enter the number of people in your group'))
    for i in range(0, group_number, 1):
        age = int(input('please enter the age of member', i))
        age = member_age.append()
        total_age = total_age + member_age[i]
    average_age = total_age / len(member_age)