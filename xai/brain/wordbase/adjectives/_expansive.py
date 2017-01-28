

#calss header
class _EXPANSIVE():
	def __init__(self,): 
		self.name = "EXPANSIVE"
		self.definitions = [u'very happy to talk to people in a friendly way: ', u'covering a large area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
