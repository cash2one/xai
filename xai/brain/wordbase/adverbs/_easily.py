

#calss header
class _EASILY():
	def __init__(self,): 
		self.name = "EASILY"
		self.definitions = [u'with no difficulty or effort: ', u'without doubt: ', u'very likely to happen or be true: ', u'quickly, or more quickly than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
