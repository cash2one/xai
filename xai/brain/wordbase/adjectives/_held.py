

#calss header
class _HELD():
	def __init__(self,): 
		self.name = "HELD"
		self.definitions = [u'kept or maintained: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
