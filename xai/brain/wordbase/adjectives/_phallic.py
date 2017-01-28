

#calss header
class _PHALLIC():
	def __init__(self,): 
		self.name = "PHALLIC"
		self.definitions = [u'representing, shaped like, or relating to the penis: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
