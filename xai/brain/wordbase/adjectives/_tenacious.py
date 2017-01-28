

#calss header
class _TENACIOUS():
	def __init__(self,): 
		self.name = "TENACIOUS"
		self.definitions = [u'holding tightly onto something, or keeping an opinion in a determined way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
