

#calss header
class _TRANSNATIONAL():
	def __init__(self,): 
		self.name = "TRANSNATIONAL"
		self.definitions = [u'involving several nations: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
