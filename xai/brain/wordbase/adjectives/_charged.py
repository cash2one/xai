

#calss header
class _CHARGED():
	def __init__(self,): 
		self.name = "CHARGED"
		self.definitions = [u'(of arguments or subjects) causing strong feelings and differences of opinion or, more generally, filled with emotion or excitement: ', u'containing a particular type of energy, especially electrical energy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
