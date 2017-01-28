

#calss header
class _OPPOSITE():
	def __init__(self,): 
		self.name = "OPPOSITE"
		self.definitions = [u'completely different: ', u'being in a position on the other side; facing: ', u'facing the speaker or stated person or thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
