

#calss header
class _URGENT():
	def __init__(self,): 
		self.name = "URGENT"
		self.definitions = [u'needing attention very soon, especially before anything else, because important: ', u"(especially of a person's actions) repeated and determined in trying to get or do something: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
