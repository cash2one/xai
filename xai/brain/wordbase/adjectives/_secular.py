

#calss header
class _SECULAR():
	def __init__(self,): 
		self.name = "SECULAR"
		self.definitions = [u'not having any connection with religion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
