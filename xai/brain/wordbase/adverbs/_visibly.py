

#calss header
class _VISIBLY():
	def __init__(self,): 
		self.name = "VISIBLY"
		self.definitions = [u'in a way that can be noticed; obviously: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
