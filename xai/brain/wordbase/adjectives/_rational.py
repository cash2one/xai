

#calss header
class _RATIONAL():
	def __init__(self,): 
		self.name = "RATIONAL"
		self.definitions = [u'based on clear thought and reason: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
