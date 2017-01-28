

#calss header
class _SLAVONIC():
	def __init__(self,): 
		self.name = "SLAVONIC"
		self.definitions = [u'of or relating to Russia, Poland, Bulgaria, and other countries of central and eastern Europe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
