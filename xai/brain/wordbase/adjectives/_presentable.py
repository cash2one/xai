

#calss header
class _PRESENTABLE():
	def __init__(self,): 
		self.name = "PRESENTABLE"
		self.definitions = [u'looking suitable or good enough, especially in the way you are dressed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
