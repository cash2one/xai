

#calss header
class _MALADJUSTED():
	def __init__(self,): 
		self.name = "MALADJUSTED"
		self.definitions = [u'A maladjusted person, usually a child, has been raised in a way that does not prepare them well for the demands of life, which often leads to problems with behaviour in the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
