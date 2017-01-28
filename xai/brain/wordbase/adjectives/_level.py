

#calss header
class _LEVEL():
	def __init__(self,): 
		self.name = "LEVEL"
		self.definitions = [u'at the same height: ', u'flat or horizontal: ', u'an amount of a liquid or substance that fills a spoon/cup but does not go above the edges, used as a measure in cooking', u'having the same value, amount, number of points, etc.: ', u'If you speak in a level voice or give someone a level look, you do it in a calm and controlled way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
