

#calss header
class _COMPACT():
	def __init__(self,): 
		self.name = "COMPACT"
		self.definitions = [u'consisting of parts that are positioned together closely or in a tidy way, using very little space: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
