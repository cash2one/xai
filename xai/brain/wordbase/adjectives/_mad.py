

#calss header
class _MAD():
	def __init__(self,): 
		self.name = "MAD"
		self.definitions = [u'mentally ill, or unable to behave in a reasonable way: ', u'extremely silly or stupid: ', u'very angry or annoyed: ', u'hurrying or excited and not having time to think or plan: ', u'to love someone or something: ', u'to want someone or something very much, or to be very interested in someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
