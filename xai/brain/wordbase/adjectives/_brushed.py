

#calss header
class _BRUSHED():
	def __init__(self,): 
		self.name = "BRUSHED"
		self.definitions = [u'A brushed material has been treated to make it soft and like fur: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
