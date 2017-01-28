

#calss header
class _VERITABLE():
	def __init__(self,): 
		self.name = "VERITABLE"
		self.definitions = [u'used to describe something as another, more exciting, interesting, or unusual thing, as a way of emphasizing its character: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
