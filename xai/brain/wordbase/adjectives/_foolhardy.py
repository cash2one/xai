

#calss header
class _FOOLHARDY():
	def __init__(self,): 
		self.name = "FOOLHARDY"
		self.definitions = [u'brave in a silly way, taking unnecessary risks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
