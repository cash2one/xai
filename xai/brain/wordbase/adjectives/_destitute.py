

#calss header
class _DESTITUTE():
	def __init__(self,): 
		self.name = "DESTITUTE"
		self.definitions = [u'without money, food, a home, or possessions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
