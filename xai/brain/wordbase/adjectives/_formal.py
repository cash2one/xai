

#calss header
class _FORMAL():
	def __init__(self,): 
		self.name = "FORMAL"
		self.definitions = [u'public or official: ', u'in appearance or by name only: ', u'Formal language, clothes, and behaviour are suitable for serious or official occasions: ', u'Formal education or training is received in a school or college: ', u'A formal garden is carefully designed and kept according to a plan, and it is not allowed to grow naturally.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
