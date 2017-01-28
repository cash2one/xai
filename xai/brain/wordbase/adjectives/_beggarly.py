

#calss header
class _BEGGARLY():
	def __init__(self,): 
		self.name = "BEGGARLY"
		self.definitions = [u'small in amount and not at all generous: ', u'like a beggar in appearance, way of life, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
