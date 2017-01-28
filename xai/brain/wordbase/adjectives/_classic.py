

#calss header
class _CLASSIC():
	def __init__(self,): 
		self.name = "CLASSIC"
		self.definitions = [u'having a high quality or standard against which other things are judged: ', u'extremely or unusually funny, bad, or annoying: ', u'having all the characteristics or qualities that you expect: ', u'bad or unpleasant, but not very surprising or unexpected: ', u'having a simple, traditional style that is always fashionable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
