

#calss header
class _COCKSURE():
	def __init__(self,): 
		self.name = "COCKSURE"
		self.definitions = [u'too confident, in a way that is slightly unpleasant or rude: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
