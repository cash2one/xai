

#calss header
class _CLERICAL():
	def __init__(self,): 
		self.name = "CLERICAL"
		self.definitions = [u'relating to work done in an office: ', u'relating to a priest or priests: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
