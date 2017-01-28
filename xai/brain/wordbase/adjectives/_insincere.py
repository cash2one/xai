

#calss header
class _INSINCERE():
	def __init__(self,): 
		self.name = "INSINCERE"
		self.definitions = [u'pretending to feel something that you do not really feel, or not meaning what you say: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
