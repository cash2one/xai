

#calss header
class _ANTIQUE():
	def __init__(self,): 
		self.name = "ANTIQUE"
		self.definitions = [u'made in an earlier period and considered to have value because of being beautiful, rare, old, or of high quality: ', u'trading or relating to antiques: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
