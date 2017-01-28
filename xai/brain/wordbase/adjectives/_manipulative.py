

#calss header
class _MANIPULATIVE():
	def __init__(self,): 
		self.name = "MANIPULATIVE"
		self.definitions = [u'A manipulative person tries to control people to their advantage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
