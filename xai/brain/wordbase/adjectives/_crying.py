

#calss header
class _CRYING():
	def __init__(self,): 
		self.name = "CRYING"
		self.definitions = [u'very serious and needing urgent attention: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
