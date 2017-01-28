

#calss header
class _RAVING():
	def __init__(self,): 
		self.name = "RAVING"
		self.definitions = [u'complete or extreme, or completely or extremely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
