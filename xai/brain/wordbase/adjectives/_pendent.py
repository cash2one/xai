

#calss header
class _PENDENT():
	def __init__(self,): 
		self.name = "PENDENT"
		self.definitions = [u'hanging from or over something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
