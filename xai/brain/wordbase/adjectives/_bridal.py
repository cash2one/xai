

#calss header
class _BRIDAL():
	def __init__(self,): 
		self.name = "BRIDAL"
		self.definitions = [u'of a woman about to be married, or of a marriage ceremony: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
