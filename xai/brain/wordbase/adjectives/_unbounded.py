

#calss header
class _UNBOUNDED():
	def __init__(self,): 
		self.name = "UNBOUNDED"
		self.definitions = [u'used to describe a positive feeling that is very great and seems to have no limits: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
