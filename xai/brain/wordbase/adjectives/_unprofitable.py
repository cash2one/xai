

#calss header
class _UNPROFITABLE():
	def __init__(self,): 
		self.name = "UNPROFITABLE"
		self.definitions = [u'not making a profit: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
