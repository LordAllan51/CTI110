# Lord
# Allan

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90

    B_score = 80

    C_score = 70

    D_score = 60

    E_score = 50

    F_score = 40
    # TO DO: define the rest of the scores

    
    score = float(input("Enter grade: "))

    if score >= A_score:
       print("Your grade is: A")
    else:
        if score > B_score:
            print("Your grade is: B")
        else:
            if score > C_score:
                print("Your grade is: C")
            else:
                if score > D_score:
                    print("Your grade is: D")
                else:
                    if score > E_score:
                        print("Your grade is: E")
                    else:
                        if score > F_score:
                            print("Your grade is: F")

                            # TO DO: finish this







# program start
main()
