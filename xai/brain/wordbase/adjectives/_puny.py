

#calss header
class _PUNY():
	def __init__(self,): 
		self.name = "PUNY"
		self.definitions = [u'small; weak; not effective: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
