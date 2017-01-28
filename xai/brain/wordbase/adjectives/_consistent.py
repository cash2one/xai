

#calss header
class _CONSISTENT():
	def __init__(self,): 
		self.name = "CONSISTENT"
		self.definitions = [u'always behaving or happening in a similar, especially positive, way: ', u'in agreement with other facts or with typical or previous behaviour, or having the same principles as something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
