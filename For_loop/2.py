#  Print the sum of the current number and the previous number

previous_no = 0
for i in range(1,6):
    sum = previous_no +i
    print("previous_number", previous_no, "current_number", i, "sum =", sum)
    previous_no = i