

#calss header
class _LITERALLY():
	def __init__(self,): 
		self.name = "LITERALLY"
		self.definitions = [u'using the real or original meaning of a word or phrase: ', u'If you translate literally, you translate each word in a text separately, without looking at how the words are used together in a phrase or sentence: ', u'used to emphasize what you are saying: ', u'simply or just: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
