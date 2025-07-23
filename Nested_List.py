if __name__ == '__main__':
    students = []
    for _ in range(int(input("Enter number of students: "))):
        name = input("Enter student name: ")
        score = float(input("Enter score: "))
        students.append([name, score])

    grades = sorted(set([s[1] for s in students]))
    second_lowest = grades[1]

    names = [s[0] for s in students if s[1] == second_lowest]
    names.sort()

    print("\nStudent(s) with the second lowest score:")
    for name in names:
        print(name)
