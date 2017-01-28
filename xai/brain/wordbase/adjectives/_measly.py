

#calss header
class _MEASLY():
	def __init__(self,): 
		self.name = "MEASLY"
		self.definitions = [u'too small in size or amount, or not enough: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
