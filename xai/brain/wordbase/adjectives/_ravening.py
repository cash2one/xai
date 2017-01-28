

#calss header
class _RAVENING():
	def __init__(self,): 
		self.name = "RAVENING"
		self.definitions = [u'(especially of wild animals) violently hunting for food: ', u'A ravening group of people try to get what they want in a forceful way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
