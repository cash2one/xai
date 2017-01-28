

#calss header
class _FEVERED():
	def __init__(self,): 
		self.name = "FEVERED"
		self.definitions = [u'unnaturally excited or active: ', u'suffering from fever: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
