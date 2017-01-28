

#calss header
class _CLUNKY():
	def __init__(self,): 
		self.name = "CLUNKY"
		self.definitions = [u'heavy and solid in an ugly way: ', u'awkward or badly done: ', u'old-fashioned or slow: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
