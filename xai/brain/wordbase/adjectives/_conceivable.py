

#calss header
class _CONCEIVABLE():
	def __init__(self,): 
		self.name = "CONCEIVABLE"
		self.definitions = [u'possible to imagine or to believe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
