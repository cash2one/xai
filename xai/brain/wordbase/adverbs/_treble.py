

#calss header
class _TREBLE():
	def __init__(self,): 
		self.name = "TREBLE"
		self.definitions = [u'three times greater in amount, number, or size: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
