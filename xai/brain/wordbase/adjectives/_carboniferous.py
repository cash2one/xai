

#calss header
class _CARBONIFEROUS():
	def __init__(self,): 
		self.name = "CARBONIFEROUS"
		self.definitions = [u'containing or producing carbon: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
