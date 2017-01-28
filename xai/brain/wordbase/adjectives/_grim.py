

#calss header
class _GRIM():
	def __init__(self,): 
		self.name = "GRIM"
		self.definitions = [u'worrying, without hope: ', u'worried and serious or sad: ', u'very unpleasant or ugly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
