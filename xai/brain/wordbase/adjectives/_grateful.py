

#calss header
class _GRATEFUL():
	def __init__(self,): 
		self.name = "GRATEFUL"
		self.definitions = [u'showing or expressing thanks, especially to another person: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
