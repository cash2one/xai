

#calss header
class _ATOMIC():
	def __init__(self,): 
		self.name = "ATOMIC"
		self.definitions = [u'relating to atoms: ', u'using the energy that is created when an atom is divided: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
