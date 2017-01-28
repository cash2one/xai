

#calss header
class _HAMMERED():
	def __init__(self,): 
		self.name = "HAMMERED"
		self.definitions = [u'very drunk']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
