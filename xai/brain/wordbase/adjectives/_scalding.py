

#calss header
class _SCALDING():
	def __init__(self,): 
		self.name = "SCALDING"
		self.definitions = [u'If a liquid is scalding, it is extremely hot: ', u'If criticism is scalding, it is very strong or violent.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
