

#calss header
class _INTERFERING():
	def __init__(self,): 
		self.name = "INTERFERING"
		self.definitions = [u"An interfering person gets involved in other people's lives in an unwanted and annoying way: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
