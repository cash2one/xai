

#calss header
class _HOPEFUL():
	def __init__(self,): 
		self.name = "HOPEFUL"
		self.definitions = [u'having hope: ', u'giving hope: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
