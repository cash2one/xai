

#calss header
class _BEST():
	def __init__(self,): 
		self.name = "BEST"
		self.definitions = [u'in the most suitable, pleasing, or satisfactory way, or to the greatest degree: ', u'to the greatest degree when used as the superlative of adjectives beginning with "good" or "well": ', u'as well as you can: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
