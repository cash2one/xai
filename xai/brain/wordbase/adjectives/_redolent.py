

#calss header
class _REDOLENT():
	def __init__(self,): 
		self.name = "REDOLENT"
		self.definitions = [u'smelling strongly of something or having qualities (especially smells) that make you think of something else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
