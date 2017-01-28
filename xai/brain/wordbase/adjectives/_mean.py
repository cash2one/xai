

#calss header
class _MEAN():
	def __init__(self,): 
		self.name = "MEAN"
		self.definitions = [u'not willing to give or share things, especially money: ', u'unkind or unpleasant: ', u'frightening and likely to become violent: ', u'very good: ', u'poor, dirty, and of bad quality: ', u'a mean number is an average number: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
