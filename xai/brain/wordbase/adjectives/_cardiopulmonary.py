

#calss header
class _CARDIOPULMONARY():
	def __init__(self,): 
		self.name = "CARDIOPULMONARY"
		self.definitions = [u'relating to the heart and lungs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
