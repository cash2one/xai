

#calss header
class _CYRILLIC():
	def __init__(self,): 
		self.name = "CYRILLIC"
		self.definitions = [u'(written in, or relating to) the alphabet used in some Slavonic languages, such as Russian']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
