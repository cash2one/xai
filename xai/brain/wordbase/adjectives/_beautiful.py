

#calss header
class _BEAUTIFUL():
	def __init__(self,): 
		self.name = "BEAUTIFUL"
		self.definitions = [u'very attractive: ', u'very pleasant: ', u'very kind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
