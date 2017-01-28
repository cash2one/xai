

#calss header
class _UNAWARE():
	def __init__(self,): 
		self.name = "UNAWARE"
		self.definitions = [u'not understanding or realizing something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
