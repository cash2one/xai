

#calss header
class _LUCKLESS():
	def __init__(self,): 
		self.name = "LUCKLESS"
		self.definitions = [u'used to describe someone who has a lot of bad luck: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
