

#calss header
class _MUNDANE():
	def __init__(self,): 
		self.name = "MUNDANE"
		self.definitions = [u'very ordinary and therefore not interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
