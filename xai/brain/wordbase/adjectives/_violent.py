

#calss header
class _VIOLENT():
	def __init__(self,): 
		self.name = "VIOLENT"
		self.definitions = [u'using force to hurt or attack: ', u'used to describe a situation or event in which people are hurt or killed: ', u'sudden and powerful: ', u'A violent colour is extremely or unpleasantly bright: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
