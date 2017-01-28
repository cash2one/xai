

#calss header
class _AMERICAN():
	def __init__(self,): 
		self.name = "AMERICAN"
		self.definitions = [u'of or relating to the United States of America: ', u'of or relating to North or South America']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
