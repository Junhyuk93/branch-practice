for i in range(1,100+1):
    if i % 3 == 0 or i % 5 == 0:
        print('fizz'*(i%3==0) + 'buzz'*(i*5==0))
    else:
        print(i)

# for i in range(100):
#     if i%15==0:
#         print('fbz')
#     elif i%5 ==0:
#         print('buz')
#     elif i%3 == 0:
#         print('fiz')
#     else:
#         print(i)
