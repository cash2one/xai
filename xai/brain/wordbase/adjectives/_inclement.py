

#calss header
class _INCLEMENT():
	def __init__(self,): 
		self.name = "INCLEMENT"
		self.definitions = [u'Inclement weather is unpleasant, especially with cold wind and rain.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
