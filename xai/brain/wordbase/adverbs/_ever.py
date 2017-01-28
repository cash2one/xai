

#calss header
class _EVER():
	def __init__(self,): 
		self.name = "EVER"
		self.definitions = [u'at any time: ', u'better, bigger, etc. than at any time before: ', u'as big, fast, etc. as at any time before: ', u'continuously: ', u'continuously since that time: ', u'in the same way as always: ', u'used at the end of a letter as a way of saying goodbye to someone you know well: ', u'used for emphasizing an adjective: ', u'in questions, used to emphasize the question word: ', u'very/a very: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
