

#calss header
class _DELUXE():
	def __init__(self,): 
		self.name = "DELUXE"
		self.definitions = [u'very comfortable and of very high quality: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
