

#calss header
class _LARGE():
	def __init__(self,): 
		self.name = "LARGE"
		self.definitions = [u'big in size or amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
