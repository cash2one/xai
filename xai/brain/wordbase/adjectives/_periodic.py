

#calss header
class _PERIODIC():
	def __init__(self,): 
		self.name = "PERIODIC"
		self.definitions = [u'happening repeatedly over a period of time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
