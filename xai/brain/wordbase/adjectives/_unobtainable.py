

#calss header
class _UNOBTAINABLE():
	def __init__(self,): 
		self.name = "UNOBTAINABLE"
		self.definitions = [u'not able to be obtained']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
