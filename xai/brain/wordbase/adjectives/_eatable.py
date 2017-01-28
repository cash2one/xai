

#calss header
class _EATABLE():
	def __init__(self,): 
		self.name = "EATABLE"
		self.definitions = [u'Food that is eatable is good enough to eat, but not excellent.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
