

#calss header
class _TANGERINE():
	def __init__(self,): 
		self.name = "TANGERINE"
		self.definitions = [u'of a dark orange colour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
