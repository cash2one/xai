

#calss header
class _LOFTY():
	def __init__(self,): 
		self.name = "LOFTY"
		self.definitions = [u'high: ', u'Lofty ideas, etc. are of a high moral standard: ', u'If you have a lofty way of behaving or talking, etc., you act as if you think you are better than other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
