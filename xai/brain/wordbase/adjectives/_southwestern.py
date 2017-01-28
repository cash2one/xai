

#calss header
class _SOUTHWESTERN():
	def __init__(self,): 
		self.name = "SOUTHWESTERN"
		self.definitions = [u'in or from the southwest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
