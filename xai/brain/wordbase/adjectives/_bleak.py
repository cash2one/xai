

#calss header
class _BLEAK():
	def __init__(self,): 
		self.name = "BLEAK"
		self.definitions = [u'If a place is bleak, it is empty, and not welcoming or attractive: ', u'Bleak weather is cold and unpleasant.', u'If a situation is bleak, there is little or no hope for the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
