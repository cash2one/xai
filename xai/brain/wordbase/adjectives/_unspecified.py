

#calss header
class _UNSPECIFIED():
	def __init__(self,): 
		self.name = "UNSPECIFIED"
		self.definitions = [u'If something is unspecified, you are not told what it is: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
