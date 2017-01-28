

#calss header
class _GASTROINTESTINAL():
	def __init__(self,): 
		self.name = "GASTROINTESTINAL"
		self.definitions = [u'in or relating to both the stomach and the intestine (= the long tube that food passes through after the stomach): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
