

#calss header
class _RECONDITE():
	def __init__(self,): 
		self.name = "RECONDITE"
		self.definitions = [u'not known about by many people and difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
