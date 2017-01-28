

#calss header
class _UNANSWERABLE():
	def __init__(self,): 
		self.name = "UNANSWERABLE"
		self.definitions = [u'If an argument or claim is unanswerable, people cannot disagree with it because it is so clearly true: ', u'(of a question) without an answer: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
