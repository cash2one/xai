

#calss header
class _INVITING():
	def __init__(self,): 
		self.name = "INVITING"
		self.definitions = [u'encouraging you to feel welcome or attracted: ', u'attractive in a way that causes unpleasant results: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
