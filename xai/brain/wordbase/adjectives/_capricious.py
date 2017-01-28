

#calss header
class _CAPRICIOUS():
	def __init__(self,): 
		self.name = "CAPRICIOUS"
		self.definitions = [u'changing mood or behaviour suddenly and unexpectedly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
