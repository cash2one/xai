

#calss header
class _WEEKLY():
	def __init__(self,): 
		self.name = "WEEKLY"
		self.definitions = [u'happening once a week or every week: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
