

#calss header
class _GLACIAL():
	def __init__(self,): 
		self.name = "GLACIAL"
		self.definitions = [u'made or left by a glacier: ', u'extremely cold: ', u'extremely unfriendly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
