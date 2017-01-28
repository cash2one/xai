

#calss header
class _CHEWY():
	def __init__(self,): 
		self.name = "CHEWY"
		self.definitions = [u'Chewy food needs to be chewed a lot before it is swallowed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
