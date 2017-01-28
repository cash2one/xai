

#calss header
class _FUTURISTIC():
	def __init__(self,): 
		self.name = "FUTURISTIC"
		self.definitions = [u'strange and very modern, or intended or seeming to come from some imagined time in the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
