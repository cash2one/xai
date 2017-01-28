

#calss header
class _ITINERANT():
	def __init__(self,): 
		self.name = "ITINERANT"
		self.definitions = [u'travelling from one place to another, usually to work for a short period: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
