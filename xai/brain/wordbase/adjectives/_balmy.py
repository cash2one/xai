

#calss header
class _BALMY():
	def __init__(self,): 
		self.name = "BALMY"
		self.definitions = [u'(of weather) pleasantly warm: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
