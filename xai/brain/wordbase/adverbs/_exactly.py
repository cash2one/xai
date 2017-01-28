

#calss header
class _EXACTLY():
	def __init__(self,): 
		self.name = "EXACTLY"
		self.definitions = [u'used when you are giving or asking for information that is completely correct: ', u'used to emphasize what you are saying: ', u'used for saying that someone or something is slightly different from a particular way of describing him, her, or it: ', u'used for saying that something is not completely true: ', u'used for saying that something is the opposite of a particular way of describing it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
