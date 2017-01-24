from my_classes._is import _is
from auto_classes.dog import dog
from auto_classes.apple import apple

x = _is()
d = dog()
a = apple()
x._is(d, a)
print(d.parents)