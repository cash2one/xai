

#calss header
class _PREMIUM():
	def __init__(self,): 
		self.name = "PREMIUM"
		self.definitions = [u'used to refer to something that is of higher than usual quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
