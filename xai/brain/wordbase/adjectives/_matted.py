

#calss header
class _MATTED():
	def __init__(self,): 
		self.name = "MATTED"
		self.definitions = [u'twisted into a firm, messy mass: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
