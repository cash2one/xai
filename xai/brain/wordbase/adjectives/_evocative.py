

#calss header
class _EVOCATIVE():
	def __init__(self,): 
		self.name = "EVOCATIVE"
		self.definitions = [u'making you remember or imagine something pleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
