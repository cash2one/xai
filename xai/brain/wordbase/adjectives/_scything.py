

#calss header
class _SCYTHING():
	def __init__(self,): 
		self.name = "SCYTHING"
		self.definitions = [u'moving sideways quickly, as if to cut through something or someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
