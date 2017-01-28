

#calss header
class _PROFUSE():
	def __init__(self,): 
		self.name = "PROFUSE"
		self.definitions = [u'produced or given in large amounts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
