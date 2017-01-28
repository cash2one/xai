

#calss header
class _INCOMPLETE():
	def __init__(self,): 
		self.name = "INCOMPLETE"
		self.definitions = [u'not having some parts, or not finished: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
