

#calss header
class _SLUGGISH():
	def __init__(self,): 
		self.name = "SLUGGISH"
		self.definitions = [u'moving or operating more slowly than usual and with less energy or power: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
