

#calss header
class _DOUBLE():
	def __init__(self,): 
		self.name = "DOUBLE"
		self.definitions = [u'in two parts or layers: ', u'to have a problem with your eyes so that you see two of everything, usually because you are drunk or ill: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
