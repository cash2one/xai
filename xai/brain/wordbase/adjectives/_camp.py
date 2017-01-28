

#calss header
class _CAMP():
	def __init__(self,): 
		self.name = "CAMP"
		self.definitions = [u'(of a man) behaving and dressing in a way that some people think is typical of a gay man: ', u'using bright colours, loud sounds, unusual behaviour, etc. in a humorous way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
