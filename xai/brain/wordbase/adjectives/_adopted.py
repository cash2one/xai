

#calss header
class _ADOPTED():
	def __init__(self,): 
		self.name = "ADOPTED"
		self.definitions = [u'An adopted child has been legally taken by another family to be taken care of as their own child: ', u'An adopted country is one where someone chooses to live although they were not born there: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
