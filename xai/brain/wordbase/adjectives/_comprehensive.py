

#calss header
class _COMPREHENSIVE():
	def __init__(self,): 
		self.name = "COMPREHENSIVE"
		self.definitions = [u'complete and including everything that is necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
