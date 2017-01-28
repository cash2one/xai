

#calss header
class _HOUSEBOUND():
	def __init__(self,): 
		self.name = "HOUSEBOUND"
		self.definitions = [u'unable to leave your home, especially because you are ill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
