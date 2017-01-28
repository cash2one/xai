

#calss header
class _STRIATED():
	def __init__(self,): 
		self.name = "STRIATED"
		self.definitions = [u'having long, thin lines, marks, or strips of colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
