

#calss header
class _SUMMERY():
	def __init__(self,): 
		self.name = "SUMMERY"
		self.definitions = [u'typical of or suitable for summer: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
