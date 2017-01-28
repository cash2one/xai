

#calss header
class _CASUAL():
	def __init__(self,): 
		self.name = "CASUAL"
		self.definitions = [u'Casual clothes are not formal or not suitable for special occasions: ', u'not taking or not seeming to take much interest: ', u'not regular or fixed: ', u'not serious or considered, or done by chance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
