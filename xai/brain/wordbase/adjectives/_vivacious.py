

#calss header
class _VIVACIOUS():
	def __init__(self,): 
		self.name = "VIVACIOUS"
		self.definitions = [u'A vivacious person, especially a woman or girl, is attractively energetic and enthusiastic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
