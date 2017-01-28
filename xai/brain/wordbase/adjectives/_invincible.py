

#calss header
class _INVINCIBLE():
	def __init__(self,): 
		self.name = "INVINCIBLE"
		self.definitions = [u'impossible to defeat or prevent from doing what is intended: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
