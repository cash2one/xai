

#calss header
class _ONWARDS():
	def __init__(self,): 
		self.name = "ONWARDS"
		self.definitions = [u'beginning at a particular time and continuing after it: ', u'If you move onwards, you continue to go forwards: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
