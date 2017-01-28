

#calss header
class _PADDED():
	def __init__(self,): 
		self.name = "PADDED"
		self.definitions = [u'containing a layer of soft material used for protection or to give shape: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
