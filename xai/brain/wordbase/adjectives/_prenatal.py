

#calss header
class _PRENATAL():
	def __init__(self,): 
		self.name = "PRENATAL"
		self.definitions = [u'relating to the medical care given to pregnant women before their babies are born: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
