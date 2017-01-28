

#calss header
class _CARDBOARD():
	def __init__(self,): 
		self.name = "CARDBOARD"
		self.definitions = [u'relating to something, usually a character in a film or play, that does not seem to be real or interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
