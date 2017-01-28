

#calss header
class _UNSHAVEN():
	def __init__(self,): 
		self.name = "UNSHAVEN"
		self.definitions = [u'not having had the hair removed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
