

#calss header
class _REGULATION():
	def __init__(self,): 
		self.name = "REGULATION"
		self.definitions = [u'according to the rules or the usual way of doing things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
