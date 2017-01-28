

#calss header
class _SUMPTUOUS():
	def __init__(self,): 
		self.name = "SUMPTUOUS"
		self.definitions = [u'luxurious and showing that you are rich: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
