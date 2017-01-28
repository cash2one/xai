

#calss header
class _NUANCED():
	def __init__(self,): 
		self.name = "NUANCED"
		self.definitions = [u'made slightly different in appearance, meaning, sound, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
