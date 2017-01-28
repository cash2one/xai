

#calss header
class _BRAINY():
	def __init__(self,): 
		self.name = "BRAINY"
		self.definitions = [u'clever: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
