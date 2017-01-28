

#calss header
class _NORMAN():
	def __init__(self,): 
		self.name = "NORMAN"
		self.definitions = [u'belonging or relating to the people from northern France, especially those who invaded (= used force to enter) England in 1066 and became its rulers, or to the buildings that were made during their rule: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
