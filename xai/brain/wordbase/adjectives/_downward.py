

#calss header
class _DOWNWARD():
	def __init__(self,): 
		self.name = "DOWNWARD"
		self.definitions = [u'moving towards a lower position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
