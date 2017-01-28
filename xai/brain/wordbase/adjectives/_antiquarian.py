

#calss header
class _ANTIQUARIAN():
	def __init__(self,): 
		self.name = "ANTIQUARIAN"
		self.definitions = [u'connected with the trade, collection, or study of old and valuable or rare objects: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
