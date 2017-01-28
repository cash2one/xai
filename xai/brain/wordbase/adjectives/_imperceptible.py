

#calss header
class _IMPERCEPTIBLE():
	def __init__(self,): 
		self.name = "IMPERCEPTIBLE"
		self.definitions = [u'unable to be noticed or felt because of being very slight: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
