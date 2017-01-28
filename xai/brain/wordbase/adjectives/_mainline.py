

#calss header
class _MAINLINE():
	def __init__(self,): 
		self.name = "MAINLINE"
		self.definitions = [u'involving beliefs, methods, etc. that are most common: ', u'relating to an important railway route between large towns or cities: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
