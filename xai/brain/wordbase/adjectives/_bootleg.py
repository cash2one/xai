

#calss header
class _BOOTLEG():
	def __init__(self,): 
		self.name = "BOOTLEG"
		self.definitions = [u'illegally made, copied, or sold: ', u'\u2192\xa0 bootcut : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
