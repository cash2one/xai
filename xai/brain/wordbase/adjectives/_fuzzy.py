

#calss header
class _FUZZY():
	def __init__(self,): 
		self.name = "FUZZY"
		self.definitions = [u'(of an image) having shapes that do not have clear edges, or (of a sound, especially from a television, radio, etc.) not clear, usually because of other unwanted noises making it difficult to hear: ', u'not clear: ', u'(of hair) in an untidy mass of tight curls: ', u'A fuzzy surface feels like short fur: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
