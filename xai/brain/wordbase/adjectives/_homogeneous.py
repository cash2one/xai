

#calss header
class _HOMOGENEOUS():
	def __init__(self,): 
		self.name = "HOMOGENEOUS"
		self.definitions = [u'consisting of parts or people that are similar to each other or are of the same type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
