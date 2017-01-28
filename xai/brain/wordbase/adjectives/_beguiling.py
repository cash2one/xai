

#calss header
class _BEGUILING():
	def __init__(self,): 
		self.name = "BEGUILING"
		self.definitions = [u'interesting or attractive, but perhaps not to be trusted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
