

#calss header
class _LOW():
	def __init__(self,): 
		self.name = "LOW"
		self.definitions = [u'not measuring much from the base to the top: ', u'close to the ground or the bottom of something: ', u'below the usual level: ', u'producing only a small amount of sound, heat, or light: ', u'of bad quality, especially when referring to something that is not as good as it should be: ', u'not considered important because of being at or near the bottom of a range of things, especially jobs or social positions: ', u'not honest or fair: ', u'(of a sound or voice) near or at the bottom of the range of sounds: ', u'unhappy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
