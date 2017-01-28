

#calss header
class _STRAGGLY():
	def __init__(self,): 
		self.name = "STRAGGLY"
		self.definitions = [u'growing or spreading out in an untidy way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
