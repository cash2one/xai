

#calss header
class _NOTEWORTHY():
	def __init__(self,): 
		self.name = "NOTEWORTHY"
		self.definitions = [u'deserving attention because of being important or interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
