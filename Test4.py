# Calculate average for Class A
marks_a = [85, 92, 78, 95, 88]
total_a = 0
for mark in marks_a:
    total_a = total_a + mark
average_a = total_a / len(marks_a)
print(f"Class A average: {average_a}")

# Now calculate average for Class B
marks_b = [70, 65, 80, 75, 90]
total_b = 0
for mark in marks_b:
    total_b = total_b + mark
average_b = total_b / len(marks_b)
print(f"Class B average: {average_b}")

# And Class C...
marks_c = [60, 72, 88, 55, 91]
total_c = 0
for mark in marks_c:
    total_c = total_c + mark
average_c = total_c / len(marks_c)
print(f"Class C average: {average_c}")