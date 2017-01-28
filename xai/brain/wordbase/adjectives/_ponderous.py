

#calss header
class _PONDEROUS():
	def __init__(self,): 
		self.name = "PONDEROUS"
		self.definitions = [u'slow and awkward because of being very heavy or large: ', u'If a book, speech, or style of writing or speaking is ponderous, it is boring because it is too slow, long, or serious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
