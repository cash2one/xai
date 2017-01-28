

#calss header
class _EXPEDITIOUS():
	def __init__(self,): 
		self.name = "EXPEDITIOUS"
		self.definitions = [u'quick: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
