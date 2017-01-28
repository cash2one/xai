

#calss header
class _SHREWD():
	def __init__(self,): 
		self.name = "SHREWD"
		self.definitions = [u'having or based on a clear understanding and good judgment of a situation, resulting in an advantage: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
