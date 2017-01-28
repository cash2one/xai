

#calss header
class _CLOISTERED():
	def __init__(self,): 
		self.name = "CLOISTERED"
		self.definitions = [u'separated from and communicating little with the outside world: ', u'surrounded by covered passages: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
