

#calss header
class _STATUESQUE():
	def __init__(self,): 
		self.name = "STATUESQUE"
		self.definitions = [u'A statuesque woman is attractively tall and large.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
