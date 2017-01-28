

#calss header
class _PROVERBIAL():
	def __init__(self,): 
		self.name = "PROVERBIAL"
		self.definitions = [u'as used in a proverb or other phrase: ', u'well known: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
