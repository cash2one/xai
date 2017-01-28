

#calss header
class _SEASONALLY():
	def __init__(self,): 
		self.name = "SEASONALLY"
		self.definitions = [u'relating to the particular season of the year: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
