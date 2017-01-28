

#calss header
class _INEFFICIENT():
	def __init__(self,): 
		self.name = "INEFFICIENT"
		self.definitions = [u'not organized, skilled, or able to work in a satisfactory way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
