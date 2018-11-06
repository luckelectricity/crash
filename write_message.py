# with open('./space.text', 'w') as message:
#   message.write('我是写入的数据\n')
#   message.write('我再写一段文字哦\n')
#   message.write('继续写入\n')

with open('./space.text', 'a') as msg:
  msg.write('附加一段文字\n')
  msg.write('继续附加一段\n')
