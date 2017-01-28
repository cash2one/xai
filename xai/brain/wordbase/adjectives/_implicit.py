

#calss header
class _IMPLICIT():
	def __init__(self,): 
		self.name = "IMPLICIT"
		self.definitions = [u'suggested but not communicated directly: ', u'complete and without any doubts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
