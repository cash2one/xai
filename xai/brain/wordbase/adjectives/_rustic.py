

#calss header
class _RUSTIC():
	def __init__(self,): 
		self.name = "RUSTIC"
		self.definitions = [u'simple and often rough in appearance; typical of the countryside: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
