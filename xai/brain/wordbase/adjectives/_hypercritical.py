

#calss header
class _HYPERCRITICAL():
	def __init__(self,): 
		self.name = "HYPERCRITICAL"
		self.definitions = [u'extremely critical (= too eager to find mistakes in everything)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
