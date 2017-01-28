

#calss header
class _DYNAMIC():
	def __init__(self,): 
		self.name = "DYNAMIC"
		self.definitions = [u'having a lot of ideas and enthusiasm: ', u'continuously changing or developing: ', u'relating to forces that produce movement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
