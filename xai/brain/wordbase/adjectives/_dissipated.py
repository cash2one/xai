

#calss header
class _DISSIPATED():
	def __init__(self,): 
		self.name = "DISSIPATED"
		self.definitions = [u'spending too much time enjoying physical pleasures and harmful activities such as drinking a lot of alcohol: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
