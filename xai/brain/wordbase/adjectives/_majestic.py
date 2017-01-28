

#calss header
class _MAJESTIC():
	def __init__(self,): 
		self.name = "MAJESTIC"
		self.definitions = [u'beautiful, powerful, or causing great admiration and respect: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
