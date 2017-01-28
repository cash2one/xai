

#calss header
class _MINIATURE():
	def __init__(self,): 
		self.name = "MINIATURE"
		self.definitions = [u'used to describe something that is a very small copy of an object: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
