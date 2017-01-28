

#calss header
class _MUTUALLY():
	def __init__(self,): 
		self.name = "MUTUALLY"
		self.definitions = [u'felt or done by two or more people or groups in the same way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
