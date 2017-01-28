

#calss header
class _UNDERDEVELOPED():
	def __init__(self,): 
		self.name = "UNDERDEVELOPED"
		self.definitions = [u'(especially of a country) without modern industry or modern services that provide transport, hospitals, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
