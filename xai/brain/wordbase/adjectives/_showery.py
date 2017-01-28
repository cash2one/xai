

#calss header
class _SHOWERY():
	def __init__(self,): 
		self.name = "SHOWERY"
		self.definitions = [u'used to describe weather with light rain that is often not continuous: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
