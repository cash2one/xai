

#calss header
class _SURE():
	def __init__(self,): 
		self.name = "SURE"
		self.definitions = [u'certainly: ', u'said when someone has thanked you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
