try:
  with open('./book.text') as book:
    content = book.read()
except FileNotFoundError:
  msg = '没有找到文件'
  print(msg)
else:
  words = content.split()
  num_words = len(words)
  print(str(num_words))
  with open('./space.text', 'a') as line:
    for word in words:
      line.write(word + ' ')
