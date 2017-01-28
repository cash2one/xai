

#calss header
class _COMMITTED():
	def __init__(self,): 
		self.name = "COMMITTED"
		self.definitions = [u'loyal and willing to give your time and energy to something that you believe in: ', u'having promised to be involved in a plan of action: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
