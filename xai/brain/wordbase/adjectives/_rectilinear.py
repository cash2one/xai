

#calss header
class _RECTILINEAR():
	def __init__(self,): 
		self.name = "RECTILINEAR"
		self.definitions = [u'moving in or formed from straight lines: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
