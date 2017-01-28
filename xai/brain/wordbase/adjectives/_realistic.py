

#calss header
class _REALISTIC():
	def __init__(self,): 
		self.name = "REALISTIC"
		self.definitions = [u'accepting things as they are in fact and not making decisions based on unlikely hopes for the future: ', u'seeming to exist or be happening in fact: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
