

#calss header
class _UNRECONSTRUCTED():
	def __init__(self,): 
		self.name = "UNRECONSTRUCTED"
		self.definitions = [u'having opinions or behaving in a way not considered to be modern or politically acceptable in modern times: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
