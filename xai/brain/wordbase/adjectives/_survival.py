

#calss header
class _SURVIVAL():
	def __init__(self,): 
		self.name = "SURVIVAL"
		self.definitions = [u'continuing to exist or wanting to continue to exist: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
