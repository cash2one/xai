

#calss header
class _INEXHAUSTIBLE():
	def __init__(self,): 
		self.name = "INEXHAUSTIBLE"
		self.definitions = [u'existing in very great amounts that will never be finished: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
