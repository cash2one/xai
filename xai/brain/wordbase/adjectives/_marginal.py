

#calss header
class _MARGINAL():
	def __init__(self,): 
		self.name = "MARGINAL"
		self.definitions = [u'very small in amount or effect: ', u'of interest to only a few people: ', u'A marginal political area or position in parliament can be won by only a small number of votes because support for the main parties is equally divided among the people voting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
