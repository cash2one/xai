

#calss header
class _DIASTOLIC():
	def __init__(self,): 
		self.name = "DIASTOLIC"
		self.definitions = [u'relating to the diastole (= the period when the main chamber of the heart is relaxed and filling with blood): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
