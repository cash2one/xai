

#calss header
class _GNARLY():
	def __init__(self,): 
		self.name = "GNARLY"
		self.definitions = [u'used to describe something extreme, especially something that is very dangerous and exciting: ', u'\u2192\xa0 gnarled : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
