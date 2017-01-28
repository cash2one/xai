

#calss header
class _ASSURED():
	def __init__(self,): 
		self.name = "ASSURED"
		self.definitions = [u'showing skill and confidence: ', u'certain to be achieved or obtained: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
