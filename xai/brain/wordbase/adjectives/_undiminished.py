

#calss header
class _UNDIMINISHED():
	def __init__(self,): 
		self.name = "UNDIMINISHED"
		self.definitions = [u'as good, strong, or important as always: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
