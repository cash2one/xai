

#calss header
class _SLANGY():
	def __init__(self,): 
		self.name = "SLANGY"
		self.definitions = [u'Slangy language contains a lot of slang expressions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
