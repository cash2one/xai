

#calss header
class _DEEP():
	def __init__(self,): 
		self.name = "DEEP"
		self.definitions = [u'a long way from the top or surface : ', u'If a football player or team plays deep, they stay a long way inside their own half of the field: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
