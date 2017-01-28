

#calss header
class _DIZZY():
	def __init__(self,): 
		self.name = "DIZZY"
		self.definitions = [u'feeling as if everything is turning around, and that you are not able to balance and may fall down: ', u'confusing and very fast: ', u'A dizzy person, especially a woman, is silly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
