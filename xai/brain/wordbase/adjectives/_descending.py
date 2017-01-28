

#calss header
class _DESCENDING():
	def __init__(self,): 
		self.name = "DESCENDING"
		self.definitions = [u'used to refer to a body part that is in a downward direction: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
