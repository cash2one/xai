

#calss header
class _SERPENTINE():
	def __init__(self,): 
		self.name = "SERPENTINE"
		self.definitions = [u'curving and twisting like a snake: ', u'complicated and difficult to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
