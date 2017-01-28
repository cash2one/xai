

#calss header
class _SPECIAL():
	def __init__(self,): 
		self.name = "SPECIAL"
		self.definitions = [u'not ordinary or usual: ', u'especially great or important, or having a quality that most similar things or people do not have: ', u'having a particular purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
