

#calss header
class _ASIDE():
	def __init__(self,): 
		self.name = "ASIDE"
		self.definitions = [u'on or to one side: ', u'If you put/set aside money, you save it for a particular purpose: ', u'If you leave or put a problem or request aside, you ignore it until you are able to solve it: ', u'except for: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
