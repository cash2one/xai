

#calss header
class _EXTERIOR():
	def __init__(self,): 
		self.name = "EXTERIOR"
		self.definitions = [u'on or from the outside: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
