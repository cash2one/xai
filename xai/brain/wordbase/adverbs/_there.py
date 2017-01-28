

#calss header
class _THERE():
	def __init__(self,): 
		self.name = "THERE"
		self.definitions = [u'(to, at, or in) that place: ', u'to arrive somewhere: ', u'to succeed: ', u'used to introduce the subject of a sentence, especially before the verbs be, seem, and appear: ', u"used to begin some children's stories written in a traditional style: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
