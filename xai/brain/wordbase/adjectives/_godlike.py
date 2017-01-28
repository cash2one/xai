

#calss header
class _GODLIKE():
	def __init__(self,): 
		self.name = "GODLIKE"
		self.definitions = [u'like God or a god in some way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
