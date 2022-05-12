#this program calculates GPA on a 5.00 scale
print('Welcome to GPA calculator 5.00')
A=5
B=4
C=3
D=2
E=1
F=0
a=5
b=4
c=3
d=2
e=1
f=0
s=0
total_credit_units=eval(input('Total credit units:'))
for i in range(eval(input('Number of course:'))):
    grade_point=eval(input('Grade:'))
    course_units=eval(input('Course unit:'))
    grade_score=grade_point*course_units
    s=s+grade_score
GPA=s/total_credit_units
print('Your current GPA is:',GPA)
if (GPA <=5.0)and (GPA >=4.5):
    print('Degree: First class honours')
elif (GPA<=4.49) and (GPA>=3.50):
    print('Degree: Second class upper')
elif (GPA<=3.49) and (GPA>=2.40):
    print('Degree: Second class lower')
else:
    print('Degree: Pass')
















































