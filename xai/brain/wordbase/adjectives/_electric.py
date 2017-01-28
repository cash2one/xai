

#calss header
class _ELECTRIC():
	def __init__(self,): 
		self.name = "ELECTRIC"
		self.definitions = [u'using electricity for power: ', u'relating to electricity: ', u'very exciting and producing strong feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
