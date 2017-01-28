

#calss header
class _SUBORDINATE():
	def __init__(self,): 
		self.name = "SUBORDINATE"
		self.definitions = [u'having a lower or less important position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
