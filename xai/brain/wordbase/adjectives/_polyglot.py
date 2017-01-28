

#calss header
class _POLYGLOT():
	def __init__(self,): 
		self.name = "POLYGLOT"
		self.definitions = [u'speaking or using several different languages: ', u'containing people from many different and distant places: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
