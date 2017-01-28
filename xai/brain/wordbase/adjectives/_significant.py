

#calss header
class _SIGNIFICANT():
	def __init__(self,): 
		self.name = "SIGNIFICANT"
		self.definitions = [u'important or noticeable: ', u'having a special meaning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
