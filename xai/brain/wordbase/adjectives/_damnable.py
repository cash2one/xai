

#calss header
class _DAMNABLE():
	def __init__(self,): 
		self.name = "DAMNABLE"
		self.definitions = [u'very annoying: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
