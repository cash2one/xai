

#calss header
class _STRAIGHT():
	def __init__(self,): 
		self.name = "STRAIGHT"
		self.definitions = [u'immediately: ', u'immediately: ', u'clearly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
