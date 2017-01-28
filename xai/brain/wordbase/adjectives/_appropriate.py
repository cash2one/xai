

#calss header
class _APPROPRIATE():
	def __init__(self,): 
		self.name = "APPROPRIATE"
		self.definitions = [u'suitable or right for a particular situation or occasion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
