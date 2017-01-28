

#calss header
class _UNAVAILING():
	def __init__(self,): 
		self.name = "UNAVAILING"
		self.definitions = [u'When an attempt to do something is unavailing, it is unsuccessful or has no positive effect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
