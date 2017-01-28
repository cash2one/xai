

#calss header
class _CAVERNOUS():
	def __init__(self,): 
		self.name = "CAVERNOUS"
		self.definitions = [u'If something is cavernous, there is a very large open space inside it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
