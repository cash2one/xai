

#calss header
class _PINPOINT():
	def __init__(self,): 
		self.name = "PINPOINT"
		self.definitions = [u'very exact: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
