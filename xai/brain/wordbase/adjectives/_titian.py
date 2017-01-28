

#calss header
class _TITIAN():
	def __init__(self,): 
		self.name = "TITIAN"
		self.definitions = [u'(of hair) reddish-gold in colour']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
