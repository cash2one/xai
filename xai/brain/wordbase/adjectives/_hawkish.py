

#calss header
class _HAWKISH():
	def __init__(self,): 
		self.name = "HAWKISH"
		self.definitions = [u'supporting the use of force in political relationships rather than discussion or other more peaceful solutions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
