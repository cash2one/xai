

#calss header
class _EXTRA():
	def __init__(self,): 
		self.name = "EXTRA"
		self.definitions = [u'added to what is normal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
