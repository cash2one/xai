

#calss header
class _SOUTHEASTERN():
	def __init__(self,): 
		self.name = "SOUTHEASTERN"
		self.definitions = [u'in or from the southeast: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
