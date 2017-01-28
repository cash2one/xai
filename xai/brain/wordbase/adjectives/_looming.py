

#calss header
class _LOOMING():
	def __init__(self,): 
		self.name = "LOOMING"
		self.definitions = [u'(of something unwanted or unpleasant) about to happen soon and causing worry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
