

#calss header
class _TODAY():
	def __init__(self,): 
		self.name = "TODAY"
		self.definitions = [u'(on) the present day: ', u'used more generally to mean the present time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
