

#calss header
class _GUSTY():
	def __init__(self,): 
		self.name = "GUSTY"
		self.definitions = [u'with sudden, strong winds: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
