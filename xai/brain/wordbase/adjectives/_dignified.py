

#calss header
class _DIGNIFIED():
	def __init__(self,): 
		self.name = "DIGNIFIED"
		self.definitions = [u'controlled, serious, and calm, and therefore deserving respect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
