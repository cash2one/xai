

#calss header
class _BIANNUAL():
	def __init__(self,): 
		self.name = "BIANNUAL"
		self.definitions = [u'happening twice a year: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
