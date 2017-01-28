

#calss header
class _CIRCUMSPECT():
	def __init__(self,): 
		self.name = "CIRCUMSPECT"
		self.definitions = [u'careful not to take risks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
