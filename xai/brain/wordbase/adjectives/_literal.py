

#calss header
class _LITERAL():
	def __init__(self,): 
		self.name = "LITERAL"
		self.definitions = [u'The literal meaning of a word is its original, basic meaning: ', u'A literal translation of a text is done by translating each word separately, without looking at how the words are used together in a phrase or sentence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
