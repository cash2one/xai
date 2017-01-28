

#calss header
class _NAMIBIAN():
	def __init__(self,): 
		self.name = "NAMIBIAN"
		self.definitions = [u'belonging to or relating to Namibia or its people']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
