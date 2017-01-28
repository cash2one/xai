

#calss header
class _COMIC():
	def __init__(self,): 
		self.name = "COMIC"
		self.definitions = [u'funny and making you want to laugh: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
