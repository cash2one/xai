

#calss header
class _FALLIBLE():
	def __init__(self,): 
		self.name = "FALLIBLE"
		self.definitions = [u'able or likely to make mistakes: ', u'A fallible object or system is likely not to work in a satisfactory way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
