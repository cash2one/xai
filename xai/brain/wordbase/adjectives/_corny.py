

#calss header
class _CORNY():
	def __init__(self,): 
		self.name = "CORNY"
		self.definitions = [u'(especially of jokes, films, stories, etc.) showing no new ideas or too often repeated, and therefore not funny or interesting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
