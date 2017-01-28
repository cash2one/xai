

#calss header
class _SOCIOECONOMIC():
	def __init__(self,): 
		self.name = "SOCIOECONOMIC"
		self.definitions = [u'related to the differences between groups of people caused mainly by their financial situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
