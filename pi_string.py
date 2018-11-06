with open('./Pi-25000000.txt') as fullPi:
  lines = fullPi.readlines()

pi_string = ''

for line in lines:
  pi_string += line.strip()

birthday = input('请输入你的生日:')
if birthday in pi_string:
  print('你的生日在pi中')
else:
  print('你的生日不在pi中')
