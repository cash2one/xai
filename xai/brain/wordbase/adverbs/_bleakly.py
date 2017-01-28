

#calss header
class _BLEAKLY():
	def __init__(self,): 
		self.name = "BLEAKLY"
		self.definitions = [u'in a way that suggests a lack of hope: ', u'in a way that is cold and empty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
