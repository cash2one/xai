

#calss header
class _INTRIGUING():
	def __init__(self,): 
		self.name = "INTRIGUING"
		self.definitions = [u'very interesting because of being unusual or mysterious: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
