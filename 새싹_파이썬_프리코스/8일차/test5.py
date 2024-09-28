import random, time

print(random.randint(1, 100))

nums = [1,2,3,4,5,6]

print(random.choice(nums))
print(random.sample(nums,3))

print("timeset: 2s")
print(time.sleep(2))
print("timeout")

#타이머
for i in range(5):
    time.sleep(1) # 1초 동안 프로그램 동작을 정지
    print(f'1초 기다린 후, {i} 출력')