
# 과제: 1부터 20까지 반복하는 과정에서 3의 배수일 경우, year를 출력하시오.
# 추가 과제: 5의 배수일 때, draem 출력
# 추가 과제2: 15의 배수일 때, yeardream
# 나머지 모든 경우는 숫자 그대로 출력

for i in range(0, 20+1):
    if i%15 == 0:
        print('yeardream')
    elif i%3 == 0:
        print('year')
    elif i%5 == 0:
        print('dream')
    else: 
        print(i)

# $ vi hello.py
# $ git status
# $ git add hello.py
# $ git commit

print('hello')
