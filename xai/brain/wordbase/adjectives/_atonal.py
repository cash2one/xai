

#calss header
class _ATONAL():
	def __init__(self,): 
		self.name = "ATONAL"
		self.definitions = [u'Atonal music is written in a way that is not based on any particular key.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
