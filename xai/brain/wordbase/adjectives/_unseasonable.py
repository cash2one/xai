

#calss header
class _UNSEASONABLE():
	def __init__(self,): 
		self.name = "UNSEASONABLE"
		self.definitions = [u'not usual or expected for the time of year: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
