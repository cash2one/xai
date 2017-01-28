

#calss header
class _RAGTAG():
	def __init__(self,): 
		self.name = "RAGTAG"
		self.definitions = [u'untidy and not similar or organized: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
