

#calss header
class _POPULAR():
	def __init__(self,): 
		self.name = "POPULAR"
		self.definitions = [u'liked, enjoyed, or supported by many people: ', u'for or involving ordinary people rather than experts or very educated people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
