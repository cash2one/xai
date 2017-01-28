

#calss header
class _SELFISH():
	def __init__(self,): 
		self.name = "SELFISH"
		self.definitions = [u'Someone who is selfish only thinks of their own advantage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
