# Q01. Grade Calculator (if-elif-else)
#
# Ask the user for a score (integer, 0-100).
# Print the letter grade using these rules:
#   90-100  → A
#   80-89   → B
#   70-79   → C
#   60-69   → D
#   Below 60 → F
#
# If the score is below 0 or above 100, print "Invalid score".
#
# Sample Input:   Enter your score: 85
# Sample Output:  Grade: B

# --- YOUR CODE HERE ---
grade=int(input("Enter a number :"))


if(90<=grade<=100):
    print("Grade: A")
elif(80<=grade<90):
    print("Grade: B")
elif(70<=grade<80):
    print("Grade: C")
elif(60<=grade<70):
    print("Grade: D")
elif(0<=grade<60):
    print("Grade: F")
else:
    print("Invalid score")
