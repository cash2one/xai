

#calss header
class _SYMBOLIC():
	def __init__(self,): 
		self.name = "SYMBOLIC"
		self.definitions = [u'representing something else: ', u'used to refer to an action that expresses or seems to express an intention or feeling, but has little practical influence on a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
