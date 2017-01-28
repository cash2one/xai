

#calss header
class _TARDY():
	def __init__(self,): 
		self.name = "TARDY"
		self.definitions = [u'slow or late in happening or arriving: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
