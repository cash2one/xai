

#calss header
class _WOBBLY():
	def __init__(self,): 
		self.name = "WOBBLY"
		self.definitions = [u'likely to wobble: ', u'uncertain what to do or changing repeatedly between two opinions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
