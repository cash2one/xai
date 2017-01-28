

#calss header
class _IMMODEST():
	def __init__(self,): 
		self.name = "IMMODEST"
		self.definitions = [u'having too high an opinion of yourself: ', u'showing too much of the body: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
