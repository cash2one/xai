

#calss header
class _CRAVEN():
	def __init__(self,): 
		self.name = "CRAVEN"
		self.definitions = [u'extremely cowardly (= not brave): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
