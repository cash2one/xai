

#calss header
class _CONTAGIOUS():
	def __init__(self,): 
		self.name = "CONTAGIOUS"
		self.definitions = [u'A contagious disease can be caught by touching someone who has the disease or a piece of infected clothing: ', u'A contagious person has a contagious disease: ', u'A contagious feeling spreads quickly among people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
