

#calss header
class _GRANDIOSE():
	def __init__(self,): 
		self.name = "GRANDIOSE"
		self.definitions = [u'larger and containing more detail than necessary, or intended to seem important or great: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
