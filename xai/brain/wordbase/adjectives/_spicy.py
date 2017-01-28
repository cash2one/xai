

#calss header
class _SPICY():
	def __init__(self,): 
		self.name = "SPICY"
		self.definitions = [u'containing strong flavours from spices: ', u'exciting and interesting, especially because of being shocking or dealing with sexual matters: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
