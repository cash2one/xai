

#calss header
class _TOASTY():
	def __init__(self,): 
		self.name = "TOASTY"
		self.definitions = [u'comfortably and pleasantly warm: ', u'like toast: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
