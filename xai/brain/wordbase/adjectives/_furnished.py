

#calss header
class _FURNISHED():
	def __init__(self,): 
		self.name = "FURNISHED"
		self.definitions = [u'containing furniture or containing furniture of a particular type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
