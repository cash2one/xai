

#calss header
class _SANGUINE():
	def __init__(self,): 
		self.name = "SANGUINE"
		self.definitions = [u"(of someone or someone's character) positive and hoping for good things: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
