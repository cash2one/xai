

#calss header
class _WHINY():
	def __init__(self,): 
		self.name = "WHINY"
		self.definitions = [u'complaining a lot in an annoying way, especially in a high, sad voice: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
