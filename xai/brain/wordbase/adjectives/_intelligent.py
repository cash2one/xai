

#calss header
class _INTELLIGENT():
	def __init__(self,): 
		self.name = "INTELLIGENT"
		self.definitions = [u'showing intelligence, or able to learn and understand things easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
