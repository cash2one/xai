

#calss header
class _CENTRIFUGAL():
	def __init__(self,): 
		self.name = "CENTRIFUGAL"
		self.definitions = [u'(of a turning object) moving away from the point around which it is turning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
