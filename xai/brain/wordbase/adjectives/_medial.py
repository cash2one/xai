

#calss header
class _MEDIAL():
	def __init__(self,): 
		self.name = "MEDIAL"
		self.definitions = [u'towards the centre of the body rather than the sides']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
