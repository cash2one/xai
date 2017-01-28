

#calss header
class _RIBALD():
	def __init__(self,): 
		self.name = "RIBALD"
		self.definitions = [u'Ribald language refers to sex in a rude but humorous way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
