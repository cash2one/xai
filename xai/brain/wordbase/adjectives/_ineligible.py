

#calss header
class _INELIGIBLE():
	def __init__(self,): 
		self.name = "INELIGIBLE"
		self.definitions = [u'not allowed to do or have something, according to particular rules: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
