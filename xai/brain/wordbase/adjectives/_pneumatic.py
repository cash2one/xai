

#calss header
class _PNEUMATIC():
	def __init__(self,): 
		self.name = "PNEUMATIC"
		self.definitions = [u'operated by air pressure: ', u'containing air: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
