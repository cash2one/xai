

#calss header
class _DEADPAN():
	def __init__(self,): 
		self.name = "DEADPAN"
		self.definitions = [u'looking or seeming serious when you are telling a joke: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
