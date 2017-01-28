

#calss header
class _SUCCINCT():
	def __init__(self,): 
		self.name = "SUCCINCT"
		self.definitions = [u'said in a clear and short way; expressing what needs to be said without unnecessary words: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
