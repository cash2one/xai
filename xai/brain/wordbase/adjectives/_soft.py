

#calss header
class _SOFT():
	def __init__(self,): 
		self.name = "SOFT"
		self.definitions = [u'not hard or firm: ', u'Soft things, especially parts of the body, are not hard or rough and feel pleasant and smooth when touched: ', u'Someone who is soft is not very healthy and strong: ', u'not forceful, loud, or easily noticed: ', u'not severe or forceful enough, especially in criticizing or punishing someone who has done something wrong: ', u'not difficult: ', u'Soft water contains a low level of minerals and allows soap to make bubbles. ', u'Soft drugs are illegal drugs that many people think are not dangerous.', u'In a soft market/economy there are more goods for sale than there are people to buy them, so prices are usually low.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
