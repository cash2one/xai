

#calss header
class _PHOTOGRAPHIC():
	def __init__(self,): 
		self.name = "PHOTOGRAPHIC"
		self.definitions = [u'relating to, used for, or produced by photography: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
