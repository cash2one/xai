

#calss header
class _BITTERSWEET():
	def __init__(self,): 
		self.name = "BITTERSWEET"
		self.definitions = [u'containing a mixture of sadness and happiness', u'tasting both bitter and sweet']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
