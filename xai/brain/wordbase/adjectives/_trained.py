

#calss header
class _TRAINED():
	def __init__(self,): 
		self.name = "TRAINED"
		self.definitions = [u'having been prepared for a particular job or activity, by learning skills, getting qualifications, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
