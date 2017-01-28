

#calss header
class _HEATHEN():
	def __init__(self,): 
		self.name = "HEATHEN"
		self.definitions = [u'(of people or their way of life, activities, and ideas) having no religion, or belonging to a religion that is not Christianity, Judaism, or Islam']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
