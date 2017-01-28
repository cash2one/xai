

#calss header
class _SADLY():
	def __init__(self,): 
		self.name = "SADLY"
		self.definitions = [u'in an unhappy way: ', u'in a way that is not satisfactory: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
