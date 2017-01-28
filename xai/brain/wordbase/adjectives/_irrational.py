

#calss header
class _IRRATIONAL():
	def __init__(self,): 
		self.name = "IRRATIONAL"
		self.definitions = [u'not using reason or clear thinking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
