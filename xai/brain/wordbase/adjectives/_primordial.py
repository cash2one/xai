

#calss header
class _PRIMORDIAL():
	def __init__(self,): 
		self.name = "PRIMORDIAL"
		self.definitions = [u'existing at or since the beginning of the world or the universe: ', u'basic and connected with an early stage of development']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
