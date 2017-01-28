

#calss header
class _ENDLESS():
	def __init__(self,): 
		self.name = "ENDLESS"
		self.definitions = [u'never finishing, or seeming never to finish: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
