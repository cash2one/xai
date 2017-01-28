

#calss header
class _PHOTOELECTRIC():
	def __init__(self,): 
		self.name = "PHOTOELECTRIC"
		self.definitions = [u'of or using an electrical current or voltage that is produced because of light']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
