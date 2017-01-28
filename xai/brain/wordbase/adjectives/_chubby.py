

#calss header
class _CHUBBY():
	def __init__(self,): 
		self.name = "CHUBBY"
		self.definitions = [u'(especially of children) fat in a pleasant and attractive way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
