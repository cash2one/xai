

#calss header
class _SUITED():
	def __init__(self,): 
		self.name = "SUITED"
		self.definitions = [u'right for someone or something: ', u'If two people who have a relationship are suited, they have a good relationship that will probably last, often because they share a lot of interests: ', u'(in compound adjectives) wearing a particular type of suit: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
