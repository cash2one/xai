

#calss header
class _WORLDWIDE():
	def __init__(self,): 
		self.name = "WORLDWIDE"
		self.definitions = [u'existing or happening in all parts of the world: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
