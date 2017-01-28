

#calss header
class _MULTILATERAL():
	def __init__(self,): 
		self.name = "MULTILATERAL"
		self.definitions = [u'involving more than two groups or countries: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
