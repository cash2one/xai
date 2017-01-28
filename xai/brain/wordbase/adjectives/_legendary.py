

#calss header
class _LEGENDARY():
	def __init__(self,): 
		self.name = "LEGENDARY"
		self.definitions = [u'very famous and admired or spoken about: ', u'from a legend: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
