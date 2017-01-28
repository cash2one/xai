

#calss header
class _NAVAL():
	def __init__(self,): 
		self.name = "NAVAL"
		self.definitions = [u"belonging to a country's navy, or relating to military ships: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
