

#calss header
class _POSITIONAL():
	def __init__(self,): 
		self.name = "POSITIONAL"
		self.definitions = [u'relating to position, especially in sports: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
