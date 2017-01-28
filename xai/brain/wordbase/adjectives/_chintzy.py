

#calss header
class _CHINTZY():
	def __init__(self,): 
		self.name = "CHINTZY"
		self.definitions = [u'decorated with a lot of chintz: ', u'cheap and of low quality: ', u'not willing to spend money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
