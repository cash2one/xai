

#calss header
class _FAILING():
	def __init__(self,): 
		self.name = "FAILING"
		self.definitions = [u'becoming weaker or less successful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
