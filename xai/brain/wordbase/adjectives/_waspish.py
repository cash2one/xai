

#calss header
class _WASPISH():
	def __init__(self,): 
		self.name = "WASPISH"
		self.definitions = [u'likely to make sharp, slightly cruel remarks; having a slightly angry and unpleasant manner: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
