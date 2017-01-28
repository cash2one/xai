

#calss header
class _MONOSYLLABIC():
	def __init__(self,): 
		self.name = "MONOSYLLABIC"
		self.definitions = [u'saying very little in a way that is rude or unfriendly: ', u'containing only one syllable']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
