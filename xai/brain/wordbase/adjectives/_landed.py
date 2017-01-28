

#calss header
class _LANDED():
	def __init__(self,): 
		self.name = "LANDED"
		self.definitions = [u'used to refer to people whose families have owned a lot of land for many generations (= family age groups): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
