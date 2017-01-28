

#calss header
class _FIRSTHAND():
	def __init__(self,): 
		self.name = "FIRSTHAND"
		self.definitions = [u'If you experience something firsthand, you experience it yourself: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
