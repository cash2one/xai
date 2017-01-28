

#calss header
class _TROUBLESOME():
	def __init__(self,): 
		self.name = "TROUBLESOME"
		self.definitions = [u'causing a lot of problems for someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
