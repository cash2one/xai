

#calss header
class _MODEST():
	def __init__(self,): 
		self.name = "MODEST"
		self.definitions = [u'not large in size or amount, or not expensive: ', u'not usually talking about or making obvious your own abilities and achievements: ', u"used to describe something, such as a woman's clothes or behaviour, that is intended to avoid attracting sexual interest: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
