

#calss header
class _TANGIBLE():
	def __init__(self,): 
		self.name = "TANGIBLE"
		self.definitions = [u'real and not imaginary; able to be shown, touched, or experienced: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
