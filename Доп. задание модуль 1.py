grades = ([5, 3, 3, 5, 4],
          [2, 2, 2, 3],
          [4, 5, 5, 2],
          [4, 4, 3],
          [5, 5, 5, 4, 5])
students = {'Johnny', 'Bilbo', 'Steve','Khendrik','Aaron'}
new_grades = grades = [sum([5, 3, 3, 5, 4])/len([5, 3, 3, 5, 4]),
                       sum([2, 2, 2, 3])/len([2, 2, 2, 3]),
                       sum([4, 5, 5, 2])/len([4, 5, 5, 2]),
                       sum([4, 4, 3])/len([4, 4, 3]),
                       sum([5, 5, 5, 4, 5])/len([5, 5, 5, 4, 5])]
new_students = students = {'Johnny': grades[2], 'Bilbo': grades[1],
                           'Steve': grades[4], 'Khendrik': grades[3],
                           'Aaron': grades[0]}
students = dict(sorted(students.items()))
print(students)