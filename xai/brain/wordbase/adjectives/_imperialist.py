

#calss header
class _IMPERIALIST():
	def __init__(self,): 
		self.name = "IMPERIALIST"
		self.definitions = [u'supporting or relating to imperialism: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
