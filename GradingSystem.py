def inputGrade():
    mark = int(input("Input Grade: "))
    if mark >= 97 and mark <= 100:
        print("Grade/Mark: 1.0 ")
        print("Description: Excellent")
    elif mark >= 94 and mark <= 96:
        print("Grade/Mark: 1.25")
        print("Description: Excellent")
    elif mark >= 91 and mark <= 93:
        print("Grade/Mark: 1.5")
        print("Description: Very Good")
    elif mark >= 88 and mark <= 90:
        print("Grade/Mark: 1.75")
        print("Description: Very Good")
    elif mark >= 85 and mark <= 87:
        print("Grade/Mark: 2.0")
        print("Description: Good")
    elif mark >= 82 and mark <= 84:
        print("Grade/Mark: 2.25")
        print("Description: Good")
    elif mark >= 79 and mark <= 81:
        print("Grade/Mark: 2.5")
        print("Description: Satisfactory")
    elif mark >= 76 and mark <= 78:
        print("Grade/Mark: 2.75")
        print("Description: Satisfactory")
    elif mark == 75:
        print("Grade/Mark: 3.0")
        print("Description: Passing")
    elif mark >= 65 and mark <= 74:
        print("Grade/Mark: 5.0")
        print("Description: Passing")
    else:
        print("Unrecognized answer please check if you input correct grade.")
    return mark

def otherRemarks():
    answer = input("Did you get an INC, W, or D as your mark? ").upper()
    if answer == "YES":
        print("\n")
        print('\033[1m' + 'INCOMPLETE' + '\033[0m')
        print("An Incomplete (Inc.) mark is temporarily given to a student who may \nqualify for passing but  has  not  taken  any  major  exam  or  its  \nequivalent. \n" )
        print('\033[1m' + 'WITHDRAWN' + '\033[0m')
        print("A Withdrawn Mark is given if the student voluntarily withdraws in writing \nfrom a subject at any time but not less than one (1) month before the final \nexamination.\n")
        print('\033[1m' + 'DROPPPED' + '\033[0m')
        print("A  Dropped  Mark  is  given  when  the  faculty  member  drops  the  student \nfrom his/her roll for having exceeded the allowable number of absences or for \nnot having attended the class since the start of the term.\n")
    elif answer == "NO":
        print('\033[1m' + 'CONGRATULATIONS' + '\033[0m' "You passed this semester, we are proud of you!")
    else:
        print("Invalid answer.")
    return answer

inputGrade()
otherRemarks()