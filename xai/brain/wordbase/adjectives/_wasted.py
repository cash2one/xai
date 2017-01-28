

#calss header
class _WASTED():
	def __init__(self,): 
		self.name = "WASTED"
		self.definitions = [u'Wasted time, money, etc. is time, money, etc. that is not used effectively because it does not produce the result you wanted: ', u'very thin and weak as a result of being ill or having no food: ', u'very drunk or illfrom drugs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
