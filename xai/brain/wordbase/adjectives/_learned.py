

#calss header
class _LEARNED():
	def __init__(self,): 
		self.name = "LEARNED"
		self.definitions = [u'A learned person has studied for a long time and has a lot of knowledge: ', u'Learned behaviour has been copied from others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
