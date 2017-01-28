

#calss header
class _CARIBBEAN():
	def __init__(self,): 
		self.name = "CARIBBEAN"
		self.definitions = [u'belonging to or relating to Caribbean islands and countries, or their people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
