

#calss header
class _UNDISPUTED():
	def __init__(self,): 
		self.name = "UNDISPUTED"
		self.definitions = [u'If something is undisputed, everyone agrees about it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
