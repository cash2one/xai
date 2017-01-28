

#calss header
class _REMOTELY():
	def __init__(self,): 
		self.name = "REMOTELY"
		self.definitions = [u'in a remote place: ', u'from a distance: ', u'in a remote or very slight way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
