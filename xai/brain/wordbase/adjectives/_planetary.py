

#calss header
class _PLANETARY():
	def __init__(self,): 
		self.name = "PLANETARY"
		self.definitions = [u'relating to planets: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
