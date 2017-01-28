

#calss header
class _PROJECTED():
	def __init__(self,): 
		self.name = "PROJECTED"
		self.definitions = [u'planned for the future or calculated based on information already known: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
