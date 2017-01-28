

#calss header
class _EXTANT():
	def __init__(self,): 
		self.name = "EXTANT"
		self.definitions = [u'used to refer to something very old that is still existing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
