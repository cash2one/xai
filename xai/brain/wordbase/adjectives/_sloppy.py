

#calss header
class _SLOPPY():
	def __init__(self,): 
		self.name = "SLOPPY"
		self.definitions = [u'(of a substance) more liquid than it should be, often in a way that is unpleasant: ', u'not taking care or making an effort: ', u'Sloppy clothes are large, loose, and do not look neat: ', u'expressing feelings of love in a way that is silly or embarrassing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
