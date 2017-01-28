

#calss header
class _FAKE():
	def __init__(self,): 
		self.name = "FAKE"
		self.definitions = [u'not real, but made to look or seem real: ', u'showing or pretending to feel emotions that are not sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
