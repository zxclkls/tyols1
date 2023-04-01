import time
class Person:
  age = 14
  height = 157.3
  money = 0
  isMale = True
  neme = 'nikita'


  def __init__(self, neme, age):
    self.neme = neme
    self.age = age
  
  def work(self, days):
  
   while days != 0:
    time.sleep(1)
    self.money += 1
    days -= 1



me = Person('Volody', 15)
friend = Person('Slavik', 16)

print(me.money)
me.work(31)
print(me.money)

