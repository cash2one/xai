

#calss header
class _FLEDGED():
	def __init__(self,): 
		self.name = "FLEDGED"
		self.definitions = [u'(of young birds) able to fly']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
