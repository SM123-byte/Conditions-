# Exam Eligilibility

medical = input("Are you medically fit (Y/N): ")
attendance = int(input("Enter the attendance: "))

if medical == 'N':
    print("You are not allowed")
else: 
    if attendance >= 75: 
        print("You are allowed")
    else:
        print("You are not allowed")