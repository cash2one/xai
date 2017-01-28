

#calss header
class _WELL():
	def __init__(self,): 
		self.name = "WELL"
		self.definitions = [u'in a good way, to a high or satisfactory standard: ', u'very much, to a great degree, or completely: ', u'used to emphasize some prepositions: ', u'used to emphasize some adjectives: ', u'very: ', u'with good reason: ', u'in addition (to): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
