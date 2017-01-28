

#calss header
class _UTMOST():
	def __init__(self,): 
		self.name = "UTMOST"
		self.definitions = [u'used to emphasize how important or serious something is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
