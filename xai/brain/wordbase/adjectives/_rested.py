

#calss header
class _RESTED():
	def __init__(self,): 
		self.name = "RESTED"
		self.definitions = [u'healthy and active after a period spent relaxing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
