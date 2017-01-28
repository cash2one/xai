

#calss header
class _SUPERIOR():
	def __init__(self,): 
		self.name = "SUPERIOR"
		self.definitions = [u'better than average or better than other people or things of the same type: ', u'A superior person believes that or acts as if they are better than other people: ', u'higher in rank or social position than others: ', u'closer to the head, further from the feet: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
