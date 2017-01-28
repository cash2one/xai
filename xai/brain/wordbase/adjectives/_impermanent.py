

#calss header
class _IMPERMANENT():
	def __init__(self,): 
		self.name = "IMPERMANENT"
		self.definitions = [u'not lasting for ever or not lasting for a long time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
