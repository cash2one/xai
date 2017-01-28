

#calss header
class _UNBIDDEN():
	def __init__(self,): 
		self.name = "UNBIDDEN"
		self.definitions = [u'not invited or wanted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
