

#calss header
class _HYDROGENATED():
	def __init__(self,): 
		self.name = "HYDROGENATED"
		self.definitions = [u'Hydrogenated fat is fat in foods that has had hydrogen added to it. Hydrogenated fats are bad for your health.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
