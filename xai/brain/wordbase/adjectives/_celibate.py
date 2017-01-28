

#calss header
class _CELIBATE():
	def __init__(self,): 
		self.name = "CELIBATE"
		self.definitions = [u'not having sexual activity, especially because you have made a religious promise not to']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
