

#calss header
class _HOLLOWLY():
	def __init__(self,): 
		self.name = "HOLLOWLY"
		self.definitions = [u'in a way that does not sound true or sincere', u'making a sound as if hitting an empty container: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
