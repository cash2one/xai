

#calss header
class _SQUEAMISH():
	def __init__(self,): 
		self.name = "SQUEAMISH"
		self.definitions = [u'easily upset or shocked by things that you find unpleasant or that you do not approve of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
