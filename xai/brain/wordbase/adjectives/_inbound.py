

#calss header
class _INBOUND():
	def __init__(self,): 
		self.name = "INBOUND"
		self.definitions = [u'travelling towards a particular point: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
