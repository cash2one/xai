

#calss header
class _SUBSTANTIAL():
	def __init__(self,): 
		self.name = "SUBSTANTIAL"
		self.definitions = [u'large in size, value, or importance: ', u'relating to the main or most important things being considered: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
