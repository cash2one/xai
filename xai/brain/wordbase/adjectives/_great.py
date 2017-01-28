

#calss header
class _GREAT():
	def __init__(self,): 
		self.name = "GREAT"
		self.definitions = [u'large in amount, size, or degree: ', u'used in names, especially to mean large or important: ', u'larger in number or amount than: ', u'famous, powerful, or important as one of a particular type: ', u'extreme: ', u'very good: ', u'used to mean that something is very bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
