

#calss header
class _ULTRAVIOLET():
	def __init__(self,): 
		self.name = "ULTRAVIOLET"
		self.definitions = [u'Ultraviolet light has a wavelength that is after the violet (= light purple) end of the range of colours that can be seen by humans. Light of this type causes the skin to become darker in the sun.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
