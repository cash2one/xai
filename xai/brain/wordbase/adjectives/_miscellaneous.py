

#calss header
class _MISCELLANEOUS():
	def __init__(self,): 
		self.name = "MISCELLANEOUS"
		self.definitions = [u'consisting of a mixture of various things that are not usually connected with each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
