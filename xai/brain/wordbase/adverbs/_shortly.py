

#calss header
class _SHORTLY():
	def __init__(self,): 
		self.name = "SHORTLY"
		self.definitions = [u'soon: ', u'a short time after or before something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
