

#calss header
class _HEREOF():
	def __init__(self,): 
		self.name = "HEREOF"
		self.definitions = [u'of the thing or document that is being talked about: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
