

#calss header
class _NEXT():
	def __init__(self,): 
		self.name = "NEXT"
		self.definitions = [u'immediately after: ', u'The time when you next do something is the first time you do it again: ', u'used when describing two people or things that are very close to each other with nothing between them: ', u"used to mean `after' when making a choice or a comparison: ", u'almost: ', u'next in order to appear or happen, often in some form of entertainment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
