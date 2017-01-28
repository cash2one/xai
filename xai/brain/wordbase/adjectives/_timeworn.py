

#calss header
class _TIMEWORN():
	def __init__(self,): 
		self.name = "TIMEWORN"
		self.definitions = [u'(no longer of interest or value because of) having been used a lot over a long period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
