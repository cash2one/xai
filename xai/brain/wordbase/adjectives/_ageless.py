

#calss header
class _AGELESS():
	def __init__(self,): 
		self.name = "AGELESS"
		self.definitions = [u'Someone or something that is ageless never looks older: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
