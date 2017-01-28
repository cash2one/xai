

#calss header
class _CHISELLED():
	def __init__(self,): 
		self.name = "CHISELLED"
		self.definitions = [u"(of a man's face or features) strong and sharp, in an attractive way: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
