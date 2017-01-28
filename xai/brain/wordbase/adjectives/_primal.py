

#calss header
class _PRIMAL():
	def __init__(self,): 
		self.name = "PRIMAL"
		self.definitions = [u'relating to the time when human life on earth began: ', u'basic and relating to an early stage of development: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
