

#calss header
class _WEEPY():
	def __init__(self,): 
		self.name = "WEEPY"
		self.definitions = [u'feeling likely to cry: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
