

#calss header
class _INDIGESTIBLE():
	def __init__(self,): 
		self.name = "INDIGESTIBLE"
		self.definitions = [u'Ingestible food is difficult or impossible for the stomach to break down: ', u'Ingestible information is difficult or impossible to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
