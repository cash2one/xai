

#calss header
class _MINUS():
	def __init__(self,): 
		self.name = "MINUS"
		self.definitions = [u'A minus number or amount is less than zero.', u'used to show that temperatures are less than zero: ', u'used after a mark given to written work to mean that it is of a slightly lower standard than that mark: ', u'used to describe a disadvantage or bad point: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
