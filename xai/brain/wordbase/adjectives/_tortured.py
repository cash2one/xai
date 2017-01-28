

#calss header
class _TORTURED():
	def __init__(self,): 
		self.name = "TORTURED"
		self.definitions = [u'involving suffering and difficulty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
