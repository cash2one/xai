

#calss header
class _NARROW():
	def __init__(self,): 
		self.name = "NARROW"
		self.definitions = [u'having a small distance from one side to the other, especially in comparison with the length: ', u'limited to a small area of interest, activity, or thought: ', u'A narrow result is one that could easily have been different because the amount by which someone failed or succeeded was very small: ', u'a situation in which you avoid danger although you very nearly do not: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
