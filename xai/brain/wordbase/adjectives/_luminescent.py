

#calss header
class _LUMINESCENT():
	def __init__(self,): 
		self.name = "LUMINESCENT"
		self.definitions = [u'producing a soft light']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
