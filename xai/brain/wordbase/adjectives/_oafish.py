

#calss header
class _OAFISH():
	def __init__(self,): 
		self.name = "OAFISH"
		self.definitions = [u'stupid, rude, or awkward: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
