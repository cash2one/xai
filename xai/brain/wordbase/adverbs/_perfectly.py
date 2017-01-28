

#calss header
class _PERFECTLY():
	def __init__(self,): 
		self.name = "PERFECTLY"
		self.definitions = [u'in a perfect way: ', u'used to emphasize the word that follows: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
