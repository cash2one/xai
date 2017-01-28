

#calss header
class _WORLDLY():
	def __init__(self,): 
		self.name = "WORLDLY"
		self.definitions = [u'relating to or consisting of physical things and ordinary life rather than spiritual things: ', u'practical and having a lot of experience of life: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
