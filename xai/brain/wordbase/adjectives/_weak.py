

#calss header
class _WEAK():
	def __init__(self,): 
		self.name = "WEAK"
		self.definitions = [u'not physically strong: ', u'not strong in character, so that you are not able to make decisions or to persuade or lead other people: ', u'A weak argument or excuse is one that is not likely to be accepted or believed: ', u'A weak drink contains a lot of water compared to its other contents, so that it does not have a strong flavour: ', u'A weak acid, alkali, or chemical base does not produce many ions (= atoms with an electrical charge) when it is dissolved in water.', u'not good enough, especially in ability, skill, or quality: ', u'A weak chin is small and does not stick out from the face.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
