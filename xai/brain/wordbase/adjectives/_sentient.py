

#calss header
class _SENTIENT():
	def __init__(self,): 
		self.name = "SENTIENT"
		self.definitions = [u'able to experience feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
