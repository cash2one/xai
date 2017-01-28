

#calss header
class _DISSATISFIED():
	def __init__(self,): 
		self.name = "DISSATISFIED"
		self.definitions = [u'not pleased with something; feeling that something is not as good as it should be: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
