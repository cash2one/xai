

#calss header
class _CALVINIST():
	def __init__(self,): 
		self.name = "CALVINIST"
		self.definitions = [u'relating to the Christian teachings of John Calvin, especially the belief that God controls what happens on earth: ', u'having severe moral standards and considering pleasure to be wrong or not necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
