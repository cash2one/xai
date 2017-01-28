

#calss header
class _WONDERFULLY():
	def __init__(self,): 
		self.name = "WONDERFULLY"
		self.definitions = [u'extremely, or extremely well: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
