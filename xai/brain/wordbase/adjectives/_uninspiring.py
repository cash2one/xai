

#calss header
class _UNINSPIRING():
	def __init__(self,): 
		self.name = "UNINSPIRING"
		self.definitions = [u'not making you feel excited or interested: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
