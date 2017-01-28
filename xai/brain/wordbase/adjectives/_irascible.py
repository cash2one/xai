

#calss header
class _IRASCIBLE():
	def __init__(self,): 
		self.name = "IRASCIBLE"
		self.definitions = [u'made angry easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
