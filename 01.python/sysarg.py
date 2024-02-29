import sys # 명령행 인수

value1 = int(sys.argv[1])
operator = sys.argv[2]
value2 = int(sys.argv[3])

if operator == '+':
    print(f'{value1}+{value2}={value1+value2}')



