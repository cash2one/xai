

#calss header
class _OUTSIZE():
	def __init__(self,): 
		self.name = "OUTSIZE"
		self.definitions = [u'(especially of clothing) much larger than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
