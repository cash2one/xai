

#calss header
class _FILIAL():
	def __init__(self,): 
		self.name = "FILIAL"
		self.definitions = [u'of a son or daughter: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
