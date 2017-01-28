

#calss header
class _INAUSPICIOUS():
	def __init__(self,): 
		self.name = "INAUSPICIOUS"
		self.definitions = [u'showing signs that something will not be successful or positive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
