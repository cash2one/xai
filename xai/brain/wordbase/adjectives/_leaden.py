

#calss header
class _LEADEN():
	def __init__(self,): 
		self.name = "LEADEN"
		self.definitions = [u'dark grey: ', u'without energy or feeling: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
