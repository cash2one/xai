

#calss header
class _NOT():
	def __init__(self,): 
		self.name = "NOT"
		self.definitions = [u'used to form a negative phrase after verbs like "be", "can", "have", "will", "must", etc., usually used in the short form "n\'t" in speech: ', u'used to give the next word or group of words a negative meaning: ', u'used after verbs like "be afraid", "hope", "suspect", etc. in short, negative replies: ', u'used to say what the situation will be if something does not happen: ', u'used to express the possibility that something might not happen: ', u'sometimes used at the end of a statement to show that you did not mean what you have said: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
