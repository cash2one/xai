

#calss header
class _CHERUBIC():
	def __init__(self,): 
		self.name = "CHERUBIC"
		self.definitions = [u'having a round, attractive face like that of a child: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
