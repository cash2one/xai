

#calss header
class _INORDINATE():
	def __init__(self,): 
		self.name = "INORDINATE"
		self.definitions = [u'much more than usual or expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
