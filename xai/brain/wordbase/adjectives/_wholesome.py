

#calss header
class _WHOLESOME():
	def __init__(self,): 
		self.name = "WHOLESOME"
		self.definitions = [u'good for you, and likely to improve your life either physically, morally, or emotionally: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
