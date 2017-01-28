

#calss header
class _INDOLENT():
	def __init__(self,): 
		self.name = "INDOLENT"
		self.definitions = [u'showing no real interest or effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
