

#calss header
class _SECRETARIAL():
	def __init__(self,): 
		self.name = "SECRETARIAL"
		self.definitions = [u'relating to the work of a secretary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
