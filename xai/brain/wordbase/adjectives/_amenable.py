

#calss header
class _AMENABLE():
	def __init__(self,): 
		self.name = "AMENABLE"
		self.definitions = [u'willing to accept or be influenced by a suggestion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
