

#calss header
class _RICH():
	def __init__(self,): 
		self.name = "RICH"
		self.definitions = [u'having a lot of money or valuable possessions: ', u'containing a large amount of a valuable natural substance such as coal, oil, or wood: ', u'containing a lot of something good or useful: ', u'Rich land or soil contains a large amount of substances that help plants to grow: ', u'used in compounds to say that someone has a lot of a particular thing, or that something contains a lot of a particular substance : ', u'containing a lot of exciting events or experiences and therefore very interesting: ', u'If the style of something such as a piece of furniture or a building is rich, it contains a lot of decoration: ', u'A rich colour, sound, smell, or taste is strong in a pleasing or attractive way: ', u'A rich material is very beautiful and valuable: ', u'If food is rich, it contains a large amount of oil, butter, eggs, or cream: ', u"used to describe someone's opinions when that person has the same bad qualities as the person they are criticizing: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
