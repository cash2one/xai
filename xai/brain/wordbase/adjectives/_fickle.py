

#calss header
class _FICKLE():
	def __init__(self,): 
		self.name = "FICKLE"
		self.definitions = [u'likely to change your opinion or your feelings suddenly and without a good reason: ', u'Fickle conditions are likely to change suddenly and without warning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
