

#calss header
class _PRECAMBRIAN():
	def __init__(self,): 
		self.name = "PRECAMBRIAN"
		self.definitions = [u'from or referring to the earliest period of time, between about 4,600 and 543 million years ago, from when the earth was formed until the first simple forms of life appeared: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
