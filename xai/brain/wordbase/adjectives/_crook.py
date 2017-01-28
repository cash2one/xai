

#calss header
class _CROOK():
	def __init__(self,): 
		self.name = "CROOK"
		self.definitions = [u'bad or ill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
