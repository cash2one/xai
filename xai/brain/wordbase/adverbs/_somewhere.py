

#calss header
class _SOMEWHERE():
	def __init__(self,): 
		self.name = "SOMEWHERE"
		self.definitions = [u'in or at a place having a position that is not stated or not known: ', u'approximately; about: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
