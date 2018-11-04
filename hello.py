# myCode = {
#   'liu': 'python',
#   'huan': 'javaScript',
#   'luck': 'jQuery',
#   'electricity': 'vue'
# }

# items keys values
# sorted() 按照key的顺序循环obj
# set 过滤重复的value (key肯定不会重复)
# for key,value in sorted(myCode.items()):
#   print(key+ ' ' +value)
# prompt = '请输入一些话,如果不想输入了就输入退出:'
# prompt += '\n请输入:'
# message = ''
# while message != '退出':
#   message = input(prompt)
#   print(message)
# import add
from add import add as a

print(a(1, 2, 3, 4, 5))
