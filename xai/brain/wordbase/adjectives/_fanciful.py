

#calss header
class _FANCIFUL():
	def __init__(self,): 
		self.name = "FANCIFUL"
		self.definitions = [u'not likely to succeed or happen in the real world: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
