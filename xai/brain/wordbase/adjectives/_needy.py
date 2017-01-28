

#calss header
class _NEEDY():
	def __init__(self,): 
		self.name = "NEEDY"
		self.definitions = [u'poor and not having enough food, clothes, etc.: ', u'wanting too much attention and love: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
