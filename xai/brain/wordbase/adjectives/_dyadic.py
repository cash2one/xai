

#calss header
class _DYADIC():
	def __init__(self,): 
		self.name = "DYADIC"
		self.definitions = [u'consisting of two parts: ', u'relating to the interaction between two people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
