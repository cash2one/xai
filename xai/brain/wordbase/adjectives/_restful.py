

#calss header
class _RESTFUL():
	def __init__(self,): 
		self.name = "RESTFUL"
		self.definitions = [u'used to describe something that produces a feeling of being calm and relaxed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
