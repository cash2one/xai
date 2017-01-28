

#calss header
class _DISENFRANCHISED():
	def __init__(self,): 
		self.name = "DISENFRANCHISED"
		self.definitions = [u'not having the right to vote, or a similar right, or having had that right taken away: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
