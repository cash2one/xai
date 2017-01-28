

#calss header
class _EFFICIENT():
	def __init__(self,): 
		self.name = "EFFICIENT"
		self.definitions = [u'working or operating quickly and effectively in an organized way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
