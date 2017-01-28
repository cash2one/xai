

#calss header
class _DISTORTED():
	def __init__(self,): 
		self.name = "DISTORTED"
		self.definitions = [u'changed from the usual, original, natural, or intended form: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
