

#calss header
class _HIGHFALUTIN():
	def __init__(self,): 
		self.name = "HIGHFALUTIN"
		self.definitions = [u'trying to seem very important or serious, but without having a good reason for doing so and looking silly as a result']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
