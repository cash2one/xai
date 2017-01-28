

#calss header
class _WHISKERED():
	def __init__(self,): 
		self.name = "WHISKERED"
		self.definitions = [u'having whiskers']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
