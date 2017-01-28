

#calss header
class _ROOMY():
	def __init__(self,): 
		self.name = "ROOMY"
		self.definitions = [u'If something such as a house or car is roomy, it has a lot of space inside it.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
