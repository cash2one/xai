

#calss header
class _MUNICIPAL():
	def __init__(self,): 
		self.name = "MUNICIPAL"
		self.definitions = [u'of or belonging to a town or city: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
