

#calss header
class _BITING():
	def __init__(self,): 
		self.name = "BITING"
		self.definitions = [u'used to describe weather that is extremely cold, especially when it causes you physical pain: ', u'used to describe words or people that criticize someone or something, usually in an unkind way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
