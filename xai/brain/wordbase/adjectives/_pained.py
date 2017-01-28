

#calss header
class _PAINED():
	def __init__(self,): 
		self.name = "PAINED"
		self.definitions = [u'If you look or sound pained, you show that you are upset or offended: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
