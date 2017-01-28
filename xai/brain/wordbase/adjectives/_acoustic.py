

#calss header
class _ACOUSTIC():
	def __init__(self,): 
		self.name = "ACOUSTIC"
		self.definitions = [u'relating to sound or hearing: ', u'used to refer to a musical instrument that is not made louder by electrical equipment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
