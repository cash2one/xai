

#calss header
class _CHEESY():
	def __init__(self,): 
		self.name = "CHEESY"
		self.definitions = [u'of bad quality or in bad taste: ', u'A cheesy smile is wide but not sincere: ', u'tasting like or of cheese: ', u"If someone's feet, shoes, or socks are cheesy, they smell unpleasant: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
