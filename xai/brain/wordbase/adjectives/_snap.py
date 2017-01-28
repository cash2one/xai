

#calss header
class _SNAP():
	def __init__(self,): 
		self.name = "SNAP"
		self.definitions = [u'done suddenly without allowing time for careful thought or preparation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
