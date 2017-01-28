

#calss header
class _REFORMATORY():
	def __init__(self,): 
		self.name = "REFORMATORY"
		self.definitions = [u'intended to change something in order to make it better: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
