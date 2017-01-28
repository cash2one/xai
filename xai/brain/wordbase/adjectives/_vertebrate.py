

#calss header
class _VERTEBRATE():
	def __init__(self,): 
		self.name = "VERTEBRATE"
		self.definitions = [u'having a spine (= back bone)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
