

#calss header
class _GIVEN():
	def __init__(self,): 
		self.name = "GIVEN"
		self.definitions = [u'already decided, arranged, or agreed: ', u'to do something regularly or as a habit: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
