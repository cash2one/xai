

#calss header
class _LIKABLE():
	def __init__(self,): 
		self.name = "LIKABLE"
		self.definitions = [u'mainly US spelling of  likeable ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
