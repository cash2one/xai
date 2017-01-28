

#calss header
class _SAGE():
	def __init__(self,): 
		self.name = "SAGE"
		self.definitions = [u'wise, especially as a result of great experience: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
