

#calss header
class _FLIRTATIOUS():
	def __init__(self,): 
		self.name = "FLIRTATIOUS"
		self.definitions = [u'behaving as if you are sexually attracted to someone, especially not in a serious way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
