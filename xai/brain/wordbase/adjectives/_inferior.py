

#calss header
class _INFERIOR():
	def __init__(self,): 
		self.name = "INFERIOR"
		self.definitions = [u'not good, or not as good as someone or something else: ', u'lower, or of lower rank: ', u'of the lower surface of a body part', u'used to refer to a body part that is below another body part: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
