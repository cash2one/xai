

#calss header
class _ALOUD():
	def __init__(self,): 
		self.name = "ALOUD"
		self.definitions = [u'in a voice loud enough to be heard: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
