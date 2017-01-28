

#calss header
class _BALLISTIC():
	def __init__(self,): 
		self.name = "BALLISTIC"
		self.definitions = [u'connected with ballistics', u'to become extremely angry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
