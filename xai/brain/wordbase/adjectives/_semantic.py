

#calss header
class _SEMANTIC():
	def __init__(self,): 
		self.name = "SEMANTIC"
		self.definitions = [u'connected with the meanings of words']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
