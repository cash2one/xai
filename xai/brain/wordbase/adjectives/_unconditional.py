

#calss header
class _UNCONDITIONAL():
	def __init__(self,): 
		self.name = "UNCONDITIONAL"
		self.definitions = [u'complete and not limited in any way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
