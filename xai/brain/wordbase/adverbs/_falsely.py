

#calss header
class _FALSELY():
	def __init__(self,): 
		self.name = "FALSELY"
		self.definitions = [u'in a way that is not true: ', u'wrongly: ', u'in a way that is not sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
