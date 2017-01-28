

#calss header
class _LIBERAL():
	def __init__(self,): 
		self.name = "LIBERAL"
		self.definitions = [u'respecting and allowing many different types of beliefs or behaviour: ', u'(of a political party or a country) believing in or allowing more personal freedom and development towards a fairer sharing of wealth and power within society', u'giving or given in a generous way: ', u'not exact; without attention to or interest in detail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
