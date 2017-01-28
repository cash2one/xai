

#calss header
class _TOO():
	def __init__(self,): 
		self.name = "TOO"
		self.definitions = [u'more than is needed or wanted; more than is suitable or enough: ', u'used before an adjective or adverb to emphasize a negative meaning: ', u'used before an adjective to emphasize a positive meaning: ', u'(especially at the end of a sentence) in addition, also: ', u'used to show surprise: ', u'very, or completely: ', u'used to emphasize a positive answer to a negative statement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
