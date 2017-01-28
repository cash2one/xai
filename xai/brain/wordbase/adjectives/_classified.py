

#calss header
class _CLASSIFIED():
	def __init__(self,): 
		self.name = "CLASSIFIED"
		self.definitions = [u'Classified information is officially stated to be secret: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
