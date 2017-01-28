

#calss header
class _BY():
	def __init__(self,): 
		self.name = "BY"
		self.definitions = [u'at the side of or (in distance or time) past: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
