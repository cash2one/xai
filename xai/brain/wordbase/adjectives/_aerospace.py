

#calss header
class _AEROSPACE():
	def __init__(self,): 
		self.name = "AEROSPACE"
		self.definitions = [u'producing or operating aircraft or spacecraft: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
