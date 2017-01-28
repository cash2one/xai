

#calss header
class _IMAGINABLE():
	def __init__(self,): 
		self.name = "IMAGINABLE"
		self.definitions = [u'possible to think of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
