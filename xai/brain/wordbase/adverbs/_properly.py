

#calss header
class _PROPERLY():
	def __init__(self,): 
		self.name = "PROPERLY"
		self.definitions = [u'correctly, or in a satisfactory way: ', u'in a socially and morally acceptable way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
