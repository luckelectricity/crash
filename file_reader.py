with open('./pi.text') as pi:
  content = pi.readlines()

pi_string = ''
for line in content:
  pi_string += line.strip()

print(pi_string)
print(len(pi_string))
