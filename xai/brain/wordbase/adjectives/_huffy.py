

#calss header
class _HUFFY():
	def __init__(self,): 
		self.name = "HUFFY"
		self.definitions = [u'angry and offended: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
