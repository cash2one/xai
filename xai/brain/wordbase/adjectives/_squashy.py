

#calss header
class _SQUASHY():
	def __init__(self,): 
		self.name = "SQUASHY"
		self.definitions = [u'soft and easy to crush: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
