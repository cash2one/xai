

#calss header
class _HOOKED():
	def __init__(self,): 
		self.name = "HOOKED"
		self.definitions = [u'enjoying something so much that you are unable to stop having it, watching it, doing it, etc.: ', u'unable to stop taking a drug: ', u'A hooked nose is large and curved.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
