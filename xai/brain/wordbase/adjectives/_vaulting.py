

#calss header
class _VAULTING():
	def __init__(self,): 
		self.name = "VAULTING"
		self.definitions = [u'a strong wish to be extremely successful, powerful, rich, etc. and a belief that this is more important than anything else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
