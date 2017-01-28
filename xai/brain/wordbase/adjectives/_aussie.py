

#calss header
class _AUSSIE():
	def __init__(self,): 
		self.name = "AUSSIE"
		self.definitions = [u'Australian, or an Australian person']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
