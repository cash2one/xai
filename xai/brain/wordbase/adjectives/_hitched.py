

#calss header
class _HITCHED():
	def __init__(self,): 
		self.name = "HITCHED"
		self.definitions = [u'to get married: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
