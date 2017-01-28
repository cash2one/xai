

#calss header
class _ASEXUAL():
	def __init__(self,): 
		self.name = "ASEXUAL"
		self.definitions = [u'without sex or sexual organs', u'having no interest in sexual relationships: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
