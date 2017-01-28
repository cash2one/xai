

#calss header
class _WARM():
	def __init__(self,): 
		self.name = "WARM"
		self.definitions = [u'having or producing a comfortably high temperature, although not hot: ', u'Warm clothes and covers are made of a material that keeps you warm: ', u'A warm colour is one that is based on or contains a colour such as red, yellow, or orange that suggests warmth.', u'a warm place: ', u'friendly and loving: ', u"(especially in children's games) almost guessing a correct answer or discovering a hidden object: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
