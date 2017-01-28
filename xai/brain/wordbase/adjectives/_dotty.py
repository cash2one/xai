

#calss header
class _DOTTY():
	def __init__(self,): 
		self.name = "DOTTY"
		self.definitions = [u'slightly strange or mentally ill: ', u'to like or love someone or something very much or be very interested in him, her, or it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
