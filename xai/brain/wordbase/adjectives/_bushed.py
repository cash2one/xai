

#calss header
class _BUSHED():
	def __init__(self,): 
		self.name = "BUSHED"
		self.definitions = [u'very tired', u'lost or confused']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
