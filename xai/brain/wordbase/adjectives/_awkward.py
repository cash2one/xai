

#calss header
class _AWKWARD():
	def __init__(self,): 
		self.name = "AWKWARD"
		self.definitions = [u'difficult to use, do, or deal with: ', u'causing problems, worry, or embarrassment: ', u'embarrassed or nervous: ', u'intentionally not helpful: ', u'moving in a way that is not natural, relaxed, or attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
