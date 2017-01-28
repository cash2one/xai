

#calss header
class _DESULTORY():
	def __init__(self,): 
		self.name = "DESULTORY"
		self.definitions = [u'without a clear plan or purpose and showing little effort or interest: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
