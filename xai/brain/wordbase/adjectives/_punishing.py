

#calss header
class _PUNISHING():
	def __init__(self,): 
		self.name = "PUNISHING"
		self.definitions = [u'very difficult and making you feel tired: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
