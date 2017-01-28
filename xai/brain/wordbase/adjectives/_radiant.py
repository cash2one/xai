

#calss header
class _RADIANT():
	def __init__(self,): 
		self.name = "RADIANT"
		self.definitions = [u'obviously very happy, or very beautiful: ', u'producing heat or light: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
