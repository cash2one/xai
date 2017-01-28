

#calss header
class _PARCHED():
	def __init__(self,): 
		self.name = "PARCHED"
		self.definitions = [u'(especially of earth or crops) dried out because of too much heat and not enough rain: ', u'extremely thirsty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
