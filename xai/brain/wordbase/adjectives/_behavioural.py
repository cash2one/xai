

#calss header
class _BEHAVIOURAL():
	def __init__(self,): 
		self.name = "BEHAVIOURAL"
		self.definitions = [u'relating to behaviour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
