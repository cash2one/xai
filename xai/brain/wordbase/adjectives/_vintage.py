

#calss header
class _VINTAGE():
	def __init__(self,): 
		self.name = "VINTAGE"
		self.definitions = [u'of high quality and lasting value, or showing the best and most typical characteristics of a particular type of thing, especially from the past: ', u'Vintage wine is of high quality and was made in a particular year and can be kept for several years in order to improve it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
