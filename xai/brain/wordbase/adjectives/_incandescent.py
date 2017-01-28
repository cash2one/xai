

#calss header
class _INCANDESCENT():
	def __init__(self,): 
		self.name = "INCANDESCENT"
		self.definitions = [u'producing a bright light from a heated filament or other part: ', u'extremely bright: ', u'showing extreme anger or happiness: ', u'extremely good, special, or skilled: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
