

#calss header
class _BLISSFUL():
	def __init__(self,): 
		self.name = "BLISSFUL"
		self.definitions = [u'extremely or completely happy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
