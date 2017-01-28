

#calss header
class _RAKISH():
	def __init__(self,): 
		self.name = "RAKISH"
		self.definitions = [u'A rakish man, especially a rich man, lives in an immoral way, especially having sex with a lot of women: ', u'confidently careless and informal: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
