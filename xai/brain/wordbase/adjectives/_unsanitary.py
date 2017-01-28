

#calss header
class _UNSANITARY():
	def __init__(self,): 
		self.name = "UNSANITARY"
		self.definitions = [u'dirty or unhealthy and therefore likely to cause disease: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
