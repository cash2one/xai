

#calss header
class _KOSHER():
	def __init__(self,): 
		self.name = "KOSHER"
		self.definitions = [u'(of food or places where food is sold, etc.) prepared or kept in conditions that follow the rules of Jewish law: ', u'legal, able to be trusted and therefore good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
