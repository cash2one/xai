

#calss header
class _CONDUCIVE():
	def __init__(self,): 
		self.name = "CONDUCIVE"
		self.definitions = [u'providing the right conditions for something good to happen or exist: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
