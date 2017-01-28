

#calss header
class _INAPPROPRIATE():
	def __init__(self,): 
		self.name = "INAPPROPRIATE"
		self.definitions = [u'unsuitable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
