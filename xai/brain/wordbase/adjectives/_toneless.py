

#calss header
class _TONELESS():
	def __init__(self,): 
		self.name = "TONELESS"
		self.definitions = [u'(of a voice) not expressing any emotion']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
