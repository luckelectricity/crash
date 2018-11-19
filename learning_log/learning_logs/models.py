from django.db import models

# Create your models here.
class Topic(models.Model):
  """用户学习的主题"""
  text = models.CharField(max_length = 200) # 标题长度,格式为字符串
  date_added = models.DateTimeField(auto_now_add=True) # 创建时间

  def __str__(self):
    return self.text

class Entry(models.Model):
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta():
    verbose_name_plural = 'entrise'

  def __str__(self):
    return self.text[:50] + '...'
