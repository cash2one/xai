

#calss header
class _PROPRIETARY():
	def __init__(self,): 
		self.name = "PROPRIETARY"
		self.definitions = [u'relating to owning something, or relating to or like an owner: ', u'Proprietary goods are made and sent out by a particular company whose name is on the product: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
