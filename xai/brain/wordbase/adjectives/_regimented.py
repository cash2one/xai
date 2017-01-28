

#calss header
class _REGIMENTED():
	def __init__(self,): 
		self.name = "REGIMENTED"
		self.definitions = [u'too organized and controlled: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
