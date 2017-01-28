

#calss header
class _UPSET():
	def __init__(self,): 
		self.name = "UPSET"
		self.definitions = [u'worried, unhappy, or angry: ', u'If you have an upset stomach you feel slightly ill, especially because of something you have eaten or drunk: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
