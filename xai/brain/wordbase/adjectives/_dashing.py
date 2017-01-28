

#calss header
class _DASHING():
	def __init__(self,): 
		self.name = "DASHING"
		self.definitions = [u'attractive in a confident, exciting, and stylish way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
