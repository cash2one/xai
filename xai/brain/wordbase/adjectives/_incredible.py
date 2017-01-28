

#calss header
class _INCREDIBLE():
	def __init__(self,): 
		self.name = "INCREDIBLE"
		self.definitions = [u'impossible, or very difficult, to believe: ', u'extremely good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
