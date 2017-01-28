

#calss header
class _WHITE():
	def __init__(self,): 
		self.name = "WHITE"
		self.definitions = [u'of a colour like that of snow, milk, or bone: ', u'having a pale face because you are not well, or you are feeling shocked: ', u'used in the names of various food and drink products, many of which are not pure white but slightly cream, yellow, grey, or transparent: ', u'of a person who has skin that is pale in colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
