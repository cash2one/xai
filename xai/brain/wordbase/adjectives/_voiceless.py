

#calss header
class _VOICELESS():
	def __init__(self,): 
		self.name = "VOICELESS"
		self.definitions = [u'If a group of people is voiceless, it does not have the power or the legal right to express their opinions: ', u'(of a speech sound) produced without making the vocal cords move']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
