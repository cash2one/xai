

#calss header
class _ROUND():
	def __init__(self,): 
		self.name = "ROUND"
		self.definitions = [u'shaped like a ball or circle, or curved: ', u'(of a number) whole or complete; given to the nearest 1, 10, 100, etc. and not as exact amounts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
