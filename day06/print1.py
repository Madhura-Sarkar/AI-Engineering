for x in range(1,11):
    print(x)

for j in range(5):
    print("*****")

    x = 5

for i in range(3):
    x = x + 2

print(x)
#  it prints 11 cuase the loop runs 3 times, and each time it adds 2 to the initial value of x (which is 5). So the calculation goes as follows:
# 1st iteration: x = 5 + 2 = 7
# 2nd iteration: x = 7 + 2 = 9
# 3rd iteration: x = 9 + 2 = 11

for k in range(2):
    print(k)
    print("hello")
    # it prints 0 and hello in the first iteration, and 1 and hello in the second iteration. The loop runs twice, with k taking the values 0 and 1 respectively.