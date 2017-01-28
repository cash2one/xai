

#calss header
class _SKILFUL():
	def __init__(self,): 
		self.name = "SKILFUL"
		self.definitions = [u'good at doing something, especially because you have practised doing it: ', u'done or made very well: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
