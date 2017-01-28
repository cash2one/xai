

#calss header
class _CLOYING():
	def __init__(self,): 
		self.name = "CLOYING"
		self.definitions = [u'too sweet and therefore unpleasant: ', u'too good or kind, or expressing feelings of love in a way that is not sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
