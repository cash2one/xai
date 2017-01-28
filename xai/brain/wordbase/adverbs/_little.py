

#calss header
class _LITTLE():
	def __init__(self,): 
		self.name = "LITTLE"
		self.definitions = [u'slightly: ', u'slowly or gradually: ', u'not much: ', u'not much more or better: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
