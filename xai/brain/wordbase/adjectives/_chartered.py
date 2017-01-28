

#calss header
class _CHARTERED():
	def __init__(self,): 
		self.name = "CHARTERED"
		self.definitions = [u'(of people who do particular jobs) having successfully finished the necessary training and exams: ', u'rented for a particular purpose: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
