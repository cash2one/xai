

#calss header
class _FRAGMENTED():
	def __init__(self,): 
		self.name = "FRAGMENTED"
		self.definitions = [u'consisting of several separate parts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
