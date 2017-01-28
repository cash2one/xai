

#calss header
class _SOLUBLE():
	def __init__(self,): 
		self.name = "SOLUBLE"
		self.definitions = [u'able to be dissolved to form a solution: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
