studentRecord = ['Jane', 'Doe', 932001234, 'Junior']
firstName = studentRecord[0]
lastName = studentRecord[1]
id = studentRecord[2]

print("Hello, " + firstName + "." + " " + "Let's calculate your test average.")
test1 = float(input('Enter Test 1 score: '))
test2 = float(input('Enter Test 2 score: '))
test3 = float(input('Enter Test 3 score: '))

average = (test1 + test2 + test3) / 3

print('Grade Report for: ' + lastName + ', ' + firstName)
print('ID: ' + str(id))
print('Current test avg: ' + str(average))
