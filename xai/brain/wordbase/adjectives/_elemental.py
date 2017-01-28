

#calss header
class _ELEMENTAL():
	def __init__(self,): 
		self.name = "ELEMENTAL"
		self.definitions = [u'showing the strong power of nature: ', u'basic or most simple, but strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
