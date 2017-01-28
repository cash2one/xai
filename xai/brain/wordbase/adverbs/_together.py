

#calss header
class _TOGETHER():
	def __init__(self,): 
		self.name = "TOGETHER"
		self.definitions = [u'with each other: ', u'If two people are described as together, they have a close romantic and often sexual relationship with each other: ', u'If two people get together or get it together, they start a sexual relationship with each other: ', u'at the same time: ', u'combined: ', u'in one place: ', u'in addition to; and also: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
